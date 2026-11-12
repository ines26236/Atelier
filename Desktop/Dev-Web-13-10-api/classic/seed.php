<?php
// Données de test Faker. Usage : php seed.php [nombre de produits, 500 par défaut]
require 'vendor/autoload.php';
require 'db.php';

$nb = (int)($argv[1] ?? 500);
$faker = Faker\Factory::create('fr_FR');
$pdo = db();

$u = $pdo->prepare('INSERT IGNORE INTO utilisateur (nom_u, email_u, mdp_u, role_u) VALUES (?,?,?,?)');
$u->execute(['Admin', 'admin@boutique.test', password_hash('admin123', PASSWORD_DEFAULT), 'admin']);

$pdo->beginTransaction();
$p = $pdo->prepare('INSERT INTO produit (type_p, designation_p, prix_ht, ppromo, date_in, stock_p) VALUES (?,?,?,?,?,?)');
for ($i = 0; $i < $nb; $i++) {
    $type = $faker->randomElement(categories());
    $p->execute([
        $type,
        $type . ' ' . $faker->company() . ' ' . strtoupper($faker->bothify('??-###')),
        $faker->randomFloat(2, 15, 2500),
        $faker->boolean(25) ? $faker->numberBetween(5, 60) : null,
        $faker->dateTimeBetween('-2 years')->format('Y-m-d'),
        $faker->numberBetween(0, 200),
    ]);
}
$pdo->commit();
echo "$nb produits créés. Admin : admin@boutique.test / admin123\n";
