<?php
require 'db.php';

if (isset($_GET['out'])) {
    session_destroy();
    header('Location: index.php');
    exit;
}

$erreur = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email'] ?? '');
    $mdp   = $_POST['mdp'] ?? '';

    // Recherche de l'utilisateur par son email avec requête préparée (protection injection SQL)
    $st = db()->prepare('SELECT * FROM utilisateur WHERE email_u = ?');
    $st->execute([$email]);
    $u = $st->fetch();

    // Vérification du mot de passe avec password_verify contre le hash bcrypt
    if ($u && password_verify($mdp, $u['mdp_u'])) {
        // Prévention de la fixation de session
        session_regenerate_id(true);
        $_SESSION['id'] = $u['id_u'];
        $_SESSION['role'] = $u['role_u'];
        $_SESSION['nom'] = $u['nom_u'];

        header('Location: ' . ($u['role_u'] === 'admin' ? 'admin.php' : 'index.php'));
        exit;
    }
    $erreur = 'Identifiants incorrects.';
}

entete('Connexion');
?>
<h1>Connexion</h1>

<?php if (isset($_GET['inscrit'])): ?>
    <p class="form-success" id="success-msg" role="status">Votre compte a bien été créé ! Vous pouvez maintenant vous connecter.</p>
<?php endif; ?>

<?php if ($erreur): ?>
    <p class="form-error" id="error-msg" role="alert"><?= e($erreur) ?></p>
<?php endif; ?>

<form method="post" class="login-form" id="form-login">
    <p>
        <label for="email">Adresse email</label>
        <input id="email" type="email" name="email" placeholder="nom@exemple.com" required value="<?= e($_POST['email'] ?? '') ?>">
    </p>
    <p>
        <label for="mdp">Mot de passe</label>
        <input id="mdp" type="password" name="mdp" placeholder="••••••••" required>
    </p>
    <button type="submit" id="btn-submit-login">Se connecter</button>
    <p style="margin-top:14px;font-size:0.9rem;color:var(--color-muted);">
        Pas encore de compte ? <a href="inscription.php">Inscrivez-vous</a>
    </p>
</form>
</main>
</body>
</html>
