<?php
require 'db.php';

// Ajout au panier : seuls l'id et la quantité viennent du client
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = (int)$_POST['id_p'];
    if (produit_get($id)) {
        $_SESSION['panier'][$id] = ($_SESSION['panier'][$id] ?? 0) + max(1, (int)$_POST['qte']);
    }
    header('Location: panier.php');
    exit;
}

// Filtres
$where = [];
$args = [];
$typeSelectionne = trim($_GET['type'] ?? '');
$recherche = trim($_GET['q'] ?? '');
$filtrePromo = isset($_GET['promo']);

if ($typeSelectionne !== '') {
    $where[] = 'type_p = ?';
    $args[] = $typeSelectionne;
}
if ($recherche !== '') {
    $where[] = 'designation_p LIKE ?';
    $args[] = '%' . $recherche . '%';
}
if ($filtrePromo) {
    $where[] = 'ppromo IS NOT NULL';
}

// Système de tri sécurisé par whitelist
$tri = $_GET['tri'] ?? 'type_asc';
$clausesTri = [
    'type_asc'   => 'type_p ASC, designation_p ASC',
    'type_desc'  => 'type_p DESC, designation_p ASC',
    'prix_asc'   => 'ROUND(prix_ht * (1 - COALESCE(ppromo, 0)/100), 2) ASC',
    'prix_desc'  => 'ROUND(prix_ht * (1 - COALESCE(ppromo, 0)/100), 2) DESC',
    'nom_asc'    => 'designation_p ASC',
    'nom_desc'   => 'designation_p DESC',
    'recent'     => 'id_p DESC',
];

$orderBy = $clausesTri[$tri] ?? $clausesTri['type_asc'];

$sql = 'SELECT * FROM produit'
     . ($where ? ' WHERE ' . implode(' AND ', $where) : '')
     . ' ORDER BY ' . $orderBy
     . ' LIMIT 100';

$st = db()->prepare($sql);
$st->execute($args);
$produits = $st->fetchAll();

$categoriesDispos = categories();

entete('Catalogue - Système de tri');
?>
<div class="catalog-header">
    <div>
        <h1>Catalogue des produits</h1>
        <p class="catalog-subtitle">Recherchez, filtrez et triez vos produits high-tech par type, prix et promotions.</p>
    </div>
</div>

<!-- Filtres rapides par type de produit (onglets) -->
<nav class="category-tabs" aria-label="Filtrer par type de produit">
    <a href="index.php?<?= http_build_query(array_merge($_GET, ['type' => ''])) ?>"
       class="tab-item <?= $typeSelectionne === '' ? 'active' : '' ?>">
       Tous les types
    </a>
    <?php foreach ($categoriesDispos as $c): ?>
        <a href="index.php?<?= http_build_query(array_merge($_GET, ['type' => $c])) ?>"
           class="tab-item <?= $typeSelectionne === $c ? 'active' : '' ?>">
           <?= e($c) ?>
        </a>
    <?php endforeach; ?>
</nav>

<!-- Formulaire de recherche et de tri -->
<form method="get" class="catalog-filters" id="filters-form">
    <div class="filter-field search-field">
        <label for="search-input" class="visually-hidden">Recherche</label>
        <input id="search-input" name="q" placeholder="Rechercher un produit..." value="<?= e($recherche) ?>">
    </div>

    <div class="filter-field">
        <label for="type-select" class="visually-hidden">Type de produit</label>
        <select id="type-select" name="type" onchange="this.form.submit()">
            <option value="">Tous les types de produit</option>
            <?php foreach ($categoriesDispos as $c): ?>
                <option value="<?= e($c) ?>" <?= $typeSelectionne === $c ? 'selected' : '' ?>><?= e($c) ?></option>
            <?php endforeach; ?>
        </select>
    </div>

    <!-- Système de Trie par type de produit et critères -->
    <div class="filter-field">
        <label for="tri-select" class="visually-hidden">Trier par</label>
        <select id="tri-select" name="tri" onchange="this.form.submit()">
            <option value="type_asc" <?= $tri === 'type_asc' ? 'selected' : '' ?>>Trier par : Type de produit (A à Z)</option>
            <option value="type_desc" <?= $tri === 'type_desc' ? 'selected' : '' ?>>Trier par : Type de produit (Z à A)</option>
            <option value="prix_asc" <?= $tri === 'prix_asc' ? 'selected' : '' ?>>Trier par : Prix croissant</option>
            <option value="prix_desc" <?= $tri === 'prix_desc' ? 'selected' : '' ?>>Trier par : Prix décroissant</option>
            <option value="nom_asc" <?= $tri === 'nom_asc' ? 'selected' : '' ?>>Trier par : Nom (A à Z)</option>
            <option value="recent" <?= $tri === 'recent' ? 'selected' : '' ?>>Trier par : Nouveautés</option>
        </select>
    </div>

    <label class="filter-checkbox">
        <input type="checkbox" name="promo" id="promo-checkbox" value="1" <?= $filtrePromo ? 'checked' : '' ?> onchange="this.form.submit()">
        Promotions
    </label>

    <button type="submit" id="btn-filtrer">Appliquer</button>

    <?php if ($typeSelectionne !== '' || $recherche !== '' || $filtrePromo || $tri !== 'type_asc'): ?>
        <a href="index.php" class="btn-reset" id="btn-reset">Réinitialiser</a>
    <?php endif; ?>
</form>

<div class="catalog-meta-bar">
    <p class="catalog-summary">
        <strong><?= count($produits) ?></strong> produit(s) trouvé(s)
        <?php if ($typeSelectionne !== ''): ?>
            dans la catégorie <span class="badge-type-active"><?= e($typeSelectionne) ?></span>
        <?php endif; ?>
        <?php if ($recherche !== ''): ?>
            pour « <em><?= e($recherche) ?></em> »
        <?php endif; ?>
    </p>
    <span class="active-sort-indicator">
        Tri actif : <strong><?= e(match($tri) {
            'type_asc' => 'Type (A-Z)',
            'type_desc' => 'Type (Z-A)',
            'prix_asc' => 'Prix croissant',
            'prix_desc' => 'Prix décroissant',
            'nom_asc' => 'Nom (A-Z)',
            'nom_desc' => 'Nom (Z-A)',
            default => 'Nouveautés'
        }) ?></strong>
    </span>
</div>

<section class="product-grid" aria-label="Produits" id="product-grid">
<?php if (empty($produits)): ?>
    <div class="empty-state">
        <p>Aucun produit ne correspond à vos critères de recherche.</p>
        <a href="index.php" class="button">Voir tous les produits</a>
    </div>
<?php else: ?>
    <?php foreach ($produits as $p): ?>
        <article class="product-card" data-type="<?= e($p['type_p']) ?>" data-id="<?= (int)$p['id_p'] ?>">
            <div class="product-card-top">
                <span class="product-type-badge"><?= e($p['type_p']) ?></span>
                <?php if ($p['ppromo']): ?>
                    <span class="badge-promo">-<?= (int)$p['ppromo'] ?>%</span>
                <?php endif; ?>
            </div>
            <img class="product-image" src="<?= e(image_url($p)) ?>" alt="<?= e($p['designation_p']) ?>" loading="lazy">
            <div class="product-info">
                <h2><?= e($p['designation_p']) ?></h2>
                <?php if ($p['ppromo']): ?>
                    <p class="product-price">
                        <s><?= number_format($p['prix_ht'], 2) ?> € HT</s>
                        <strong><?= number_format(prix_final($p), 2) ?> € HT</strong>
                    </p>
                <?php else: ?>
                    <p class="product-price">
                        <strong><?= number_format($p['prix_ht'], 2) ?> € HT</strong>
                    </p>
                <?php endif; ?>

                <?php if ($p['stock_p'] > 0): ?>
                    <form method="post" class="add-to-cart-form">
                        <input type="hidden" name="id_p" value="<?= (int)$p['id_p'] ?>">
                        <input type="number" name="qte" value="1" min="1" max="<?= (int)$p['stock_p'] ?>" aria-label="Quantité">
                        <button type="submit" class="btn-add-cart">Ajouter</button>
                    </form>
                <?php else: ?>
                    <p class="stock-unavailable">Rupture de stock</p>
                <?php endif; ?>
            </div>
        </article>
    <?php endforeach; ?>
<?php endif; ?>
</section>
</main>
</body>
</html>
