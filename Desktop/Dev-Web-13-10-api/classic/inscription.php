<?php
require 'db.php';

$erreurs = [];
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nom   = trim($_POST['nom'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $mdp   = $_POST['mdp'] ?? '';

    if ($nom === '')                                $erreurs[] = 'Nom requis.';
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $erreurs[] = 'Email invalide.';
    if (strlen($mdp) < 6)                           $erreurs[] = 'Mot de passe : 6 caractères minimum.';

    if (!$erreurs) {
        try {
            // Le rôle est toujours 'client' pour les inscriptions publiques
            // Sécurité : mot de passe haché avec l'algorithme standard bcrypt (BCRYPT / PASSWORD_DEFAULT)
            $hash = password_hash($mdp, PASSWORD_DEFAULT);
            $st = db()->prepare('INSERT INTO utilisateur (nom_u, email_u, mdp_u, role_u) VALUES (?,?,?,?)');
            $st->execute([$nom, $email, $hash, 'client']);

            header('Location: login.php?inscrit=1');
            exit;
        } catch (PDOException $ex) {
            if ($ex->getCode() !== '23000') throw $ex;   // 23000 = email déjà existant (contrainte UNIQUE)
            $erreurs[] = 'Cet email est déjà utilisé.';
        }
    }
}

entete('Inscription');
?>
<h1>Inscription</h1>
<?php foreach ($erreurs as $err): ?>
    <p class="form-error" role="alert" id="error-msg"><?= e($err) ?></p>
<?php endforeach; ?>

<form method="post" class="login-form" id="form-inscription">
    <p>
        <label for="nom">Nom complet</label>
        <input id="nom" name="nom" placeholder="Votre nom" required value="<?= e($_POST['nom'] ?? '') ?>">
    </p>
    <p>
        <label for="email">Adresse email</label>
        <input id="email" type="email" name="email" placeholder="nom@exemple.com" required value="<?= e($_POST['email'] ?? '') ?>">
    </p>
    <p>
        <label for="mdp">Mot de passe (6 car. min.)</label>
        <input id="mdp" type="password" name="mdp" placeholder="••••••••" required minlength="6">
    </p>
    <button type="submit" id="btn-submit-inscription">Créer mon compte</button>
    <p style="margin-top:14px;font-size:0.9rem;color:var(--color-muted);">
        Vous avez déjà un compte ? <a href="login.php">Connectez-vous</a>
    </p>
</form>
</main>
</body>
</html>
