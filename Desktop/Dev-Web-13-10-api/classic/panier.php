<?php
require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['vider'])) {
        unset($_SESSION['panier']);
    } else {
        foreach ($_POST['qte'] ?? [] as $id => $qte) {   // quantités uniquement, jamais de prix
            if ((int)$qte > 0) $_SESSION['panier'][(int)$id] = (int)$qte;
            else unset($_SESSION['panier'][(int)$id]);
        }
    }
    header('Location: panier.php');
    exit;
}

$c = panier_calculer();
entete('Panier');
?>
<h1>Panier</h1>
<?php if (!$c['lignes']): ?>
    <p class="empty-state">Votre panier est vide.</p>
<?php else: ?>
<form method="post" class="cart-form">
    <div class="table-wrapper">
    <table class="data-table cart-table">
        <tr><th>Produit</th><th>Prix unit. HT</th><th>Qté</th><th>Total HT</th></tr>
        <?php foreach ($c['lignes'] as $l): ?>
        <tr>
            <td><?= e($l['p']['designation_p']) ?></td>
            <td><?= number_format(prix_final($l['p']), 2) ?> €</td>
            <td><input class="quantity-input" type="number" name="qte[<?= $l['p']['id_p'] ?>]" value="<?= $l['qte'] ?>" min="0" max="<?= $l['p']['stock_p'] ?>"></td>
            <td><?= number_format($l['total'], 2) ?> €</td>
        </tr>
        <?php endforeach; ?>
        <tr><td colspan="3">Sous-total HT</td><td><?= number_format($c['sous_total'], 2) ?> €</td></tr>
        <tr><td colspan="3">Expédition HT</td><td><?= $c['port'] ? number_format($c['port'], 2) . ' €' : 'Offerte' ?></td></tr>
        <tr><td colspan="3">TVA (<?= TVA * 100 ?>%)</td><td><?= number_format($c['tva'], 2) ?> €</td></tr>
        <tr><th colspan="3">Total TTC</th><th><?= number_format($c['ttc'], 2) ?> €</th></tr>
    </table>
    </div>
    <button>Mettre à jour</button>
    <button name="vider" value="1">Vider</button>
</form>
<?php endif; ?>
</main>
</body>
</html>
