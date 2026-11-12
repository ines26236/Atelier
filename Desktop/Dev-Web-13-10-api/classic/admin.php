<?php
require 'db.php';

if (!est_admin()) {
    header('Location: login.php');
    exit;
}

$id = (int)($_GET['id'] ?? 0);
$erreurs = [];

// Suppression
if (isset($_POST['supprimer'])) {
    $p = produit_get((int)$_POST['supprimer']);
    if ($p) {
        db()->prepare('DELETE FROM produit WHERE id_p = ?')->execute([$p['id_p']]);
        if ($p['image_p']) @unlink(__DIR__ . '/uploads/' . $p['image_p']);
    }
    header('Location: admin.php');
    exit;
}

// Création / modification
if (isset($_POST['enregistrer'])) {
    $type  = $_POST['type_p'] ?? '';
    $desig = trim($_POST['designation_p'] ?? '');
    $prix  = $_POST['prix_ht'] ?? '';
    $promo = ($_POST['ppromo'] ?? '') === '' ? null : (int)$_POST['ppromo'];
    $stock = (int)($_POST['stock_p'] ?? 0);

    if (!in_array($type, categories(), true))        $erreurs[] = 'Catégorie invalide.';
    if ($desig === '')                               $erreurs[] = 'Désignation requise.';
    if (!is_numeric($prix) || $prix < 0)             $erreurs[] = 'Prix invalide.';
    if ($promo !== null && ($promo < 1 || $promo > 99)) $erreurs[] = 'Promo : 1 à 99 ou vide.';
    if ($stock < 0)                                  $erreurs[] = 'Stock invalide.';

    // Image (optionnelle) : type vérifié sur le contenu du fichier
    $image = null;
    if (!empty($_FILES['image']['name'])) {
        $ext = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp']
               [(new finfo(FILEINFO_MIME_TYPE))->file($_FILES['image']['tmp_name'])] ?? null;
        if (!$ext || $_FILES['image']['size'] > 2 * 1024 * 1024 || $_FILES['image']['error']) {
            $erreurs[] = 'Image invalide (JPEG/PNG/WebP, 2 Mo max).';
        } else {
            $image = bin2hex(random_bytes(8)) . '.' . $ext;
            move_uploaded_file($_FILES['image']['tmp_name'], __DIR__ . '/uploads/' . $image);
        }
    }

    if (!$erreurs) {
        if ($id && ($old = produit_get($id))) {
            db()->prepare('UPDATE produit SET type_p=?, designation_p=?, prix_ht=?, ppromo=?, stock_p=?, image_p=COALESCE(?, image_p) WHERE id_p=?')
                ->execute([$type, $desig, $prix, $promo, $stock, $image, $id]);
            if ($image && $old['image_p']) @unlink(__DIR__ . '/uploads/' . $old['image_p']);
        } else {
            db()->prepare('INSERT INTO produit (type_p, designation_p, prix_ht, ppromo, stock_p, image_p, date_in) VALUES (?,?,?,?,?,?,CURDATE())')
                ->execute([$type, $desig, $prix, $promo, $stock, $image]);
        }
        header('Location: admin.php');
        exit;
    }
}

$edit = $id ? produit_get($id) : null;
$v = $edit ?? ['type_p' => '', 'designation_p' => '', 'prix_ht' => '', 'ppromo' => '', 'stock_p' => 0];
$produits = db()->query('SELECT * FROM produit ORDER BY id_p DESC LIMIT 100')->fetchAll();

entete('Administration');
?>
<h1>Administration des produits</h1>

<h2><?= $edit ? 'Modifier le produit #' . $id : 'Ajouter un produit' ?></h2>
<?php foreach ($erreurs as $err): ?><p class="form-error" role="alert"><?= e($err) ?></p><?php endforeach; ?>
<form method="post" enctype="multipart/form-data" class="product-form">
    <p><input name="designation_p" placeholder="Désignation" required value="<?= e($v['designation_p']) ?>"></p>
    <p>
        <select name="type_p" required>
            <option value="">Catégorie…</option>
            <?php foreach (categories() as $c): ?>
                <option <?= $v['type_p'] === $c ? 'selected' : '' ?>><?= e($c) ?></option>
            <?php endforeach; ?>
        </select>
    </p>
    <p><input name="prix_ht" type="number" step="0.01" min="0" placeholder="Prix HT" required value="<?= e($v['prix_ht']) ?>"></p>
    <p><input name="ppromo" type="number" min="1" max="99" placeholder="% promo (vide = aucune)" value="<?= e($v['ppromo']) ?>"></p>
    <p><input name="stock_p" type="number" min="0" placeholder="Stock" required value="<?= e($v['stock_p']) ?>"></p>
    <p><input type="file" name="image" accept="image/jpeg,image/png,image/webp"></p>
    <button name="enregistrer" value="1">Enregistrer</button>
    <?php if ($edit): ?><a href="admin.php">Annuler</a><?php endif; ?>
</form>

<h2>Produits</h2>
<div class="table-wrapper">
<table class="data-table admin-table">
    <tr><th>#</th><th>Image</th><th>Désignation</th><th>Type</th><th>Prix HT</th><th>Promo</th><th>Stock</th><th></th></tr>
    <?php foreach ($produits as $p): ?>
    <tr>
        <td><?= $p['id_p'] ?></td>
        <td><img src="<?= e(image_url($p)) ?>" width="48" alt=""></td>
        <td><?= e($p['designation_p']) ?></td>
        <td><?= e($p['type_p']) ?></td>
        <td><?= number_format($p['prix_ht'], 2) ?> €</td>
        <td><?= $p['ppromo'] ? '-' . $p['ppromo'] . '%' : '' ?></td>
        <td><?= $p['stock_p'] ?></td>
        <td>
            <a href="admin.php?id=<?= $p['id_p'] ?>">Modifier</a>
            <form method="post" class="inline-form" onsubmit="return confirm('Supprimer ?')">
                <button name="supprimer" value="<?= $p['id_p'] ?>">Supprimer</button>
            </form>
        </td>
    </tr>
    <?php endforeach; ?>
</table>
</div>
</main>
</body>
</html>
