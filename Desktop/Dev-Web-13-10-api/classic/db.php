<?php
// Connexion PDO unique + fonctions métier. Inclus par toutes les pages.
session_start();

const TVA = 0.20;
const FRAIS_PORT = 5.90;      // HT
const PORT_GRATUIT_DES = 50;  // sous-total HT

function db(): PDO
{
    static $pdo = null;
    return $pdo ??= new PDO('mysql:host=127.0.0.1;dbname=2026_m1;charset=utf8mb4', 'root', '', [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
}

function e($s): string
{
    return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8');
}

function categories(): array
{
    return array_column(json_decode(file_get_contents(__DIR__ . '/categories.json'), true), 'categorie');
}

function prix_final(array $p): float
{
    return round($p['prix_ht'] * (1 - ($p['ppromo'] ?? 0) / 100), 2);
}

function image_url(array $p): string
{
    if (!empty($p['image_p']) && is_file(__DIR__ . '/uploads/' . $p['image_p'])) {
        return 'uploads/' . $p['image_p'];
    }

    // Association automatique d'une illustration par type de produit
    $type = mb_strtolower(trim($p['type_p'] ?? ''));
    $mapping = [
        'smartphone'          => 'assets/img/smartphone.svg',
        'ordinateur portable' => 'assets/img/ordinateur.svg',
        'casque audio'        => 'assets/img/casque.svg',
        'montre connectée'    => 'assets/img/montre.svg',
        'montre connectee'    => 'assets/img/montre.svg',
        'tablette'            => 'assets/img/tablette.svg',
        'caméra'              => 'assets/img/camera.svg',
        'camera'              => 'assets/img/camera.svg',
    ];

    if (isset($mapping[$type]) && is_file(__DIR__ . '/' . $mapping[$type])) {
        return $mapping[$type];
    }

    return 'assets/img/placeholder.svg';
}

function produit_get(int $id): ?array
{
    $st = db()->prepare('SELECT * FROM produit WHERE id_p = ?');
    $st->execute([$id]);
    return $st->fetch() ?: null;
}

function est_admin(): bool
{
    return ($_SESSION['role'] ?? '') === 'admin';
}

/** Panier : la session ne contient que id => quantité. Les prix viennent toujours de la base. */
function panier_calculer(): array
{
    $lignes = [];
    $sous_total = 0;
    foreach ($_SESSION['panier'] ?? [] as $id => $qte) {
        $p = produit_get($id);
        if (!$p || $p['stock_p'] < 1) {
            unset($_SESSION['panier'][$id]);
            continue;
        }
        $qte = min($qte, $p['stock_p']);
        $total = round(prix_final($p) * $qte, 2);
        $sous_total += $total;
        $lignes[] = ['p' => $p, 'qte' => $qte, 'total' => $total];
    }
    $port = ($sous_total == 0 || $sous_total >= PORT_GRATUIT_DES) ? 0 : FRAIS_PORT;
    $tva = round(($sous_total + $port) * TVA, 2);
    return ['lignes' => $lignes, 'sous_total' => $sous_total, 'port' => $port, 'tva' => $tva,
            'ttc' => round($sous_total + $port + $tva, 2)];
}

function entete(string $titre): void
{ ?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Boutique en ligne de produits high-tech">
    <meta name="author" content="Groupe Dev Web">
    <meta name="copyright" content="© 2026 Groupe Dev Web">
    <title><?= e($titre) ?></title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
    <nav class="site-nav" aria-label="Navigation principale">
        <a class="site-brand" href="index.php">Boutique</a>
        <div class="site-nav-links">
            <a href="index.php">Catalogue</a>
            <a href="panier.php">Panier <span class="cart-count"><?= array_sum($_SESSION['panier'] ?? []) ?></span></a>
            <?php if (est_admin()): ?><a href="admin.php">Administration</a><a href="utilisateurs.php">Utilisateurs</a><?php endif; ?>
            <?php if (isset($_SESSION['role'])): ?><a href="login.php?out=1">Déconnexion</a>
            <?php else: ?><a href="login.php">Connexion</a><a href="inscription.php">Inscription</a><?php endif; ?>
        </div>
    </nav>
</header>
<main class="page-content">
<?php }
