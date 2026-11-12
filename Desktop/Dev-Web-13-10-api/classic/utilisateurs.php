<?php
require 'db.php';

if (!est_admin()) {
    header('Location: login.php');
    exit;
}

$moi = (int)($_SESSION['id'] ?? 0);
$id = (int)($_GET['id'] ?? 0);
$erreurs = [];

// il doit toujours rester au moins un admin
function nb_admins(): int
{
    return (int)db()->query("SELECT COUNT(*) FROM utilisateur WHERE role_u = 'admin'")->fetchColumn();
}

function role_de(int $id): ?string
{
    $st = db()->prepare('SELECT role_u FROM utilisateur WHERE id_u = ?');
    $st->execute([$id]);
    return $st->fetchColumn() ?: null;
}

// Suppression (interdite pour son propre compte et pour le dernier admin)
if (isset($_POST['supprimer'])) {
    $cible = (int)$_POST['supprimer'];
    if ($cible === $moi) {
        $erreurs[] = 'Vous ne pouvez pas supprimer votre propre compte.';
    } elseif (role_de($cible) === 'admin' && nb_admins() <= 1) {
        $erreurs[] = 'Impossible de supprimer le dernier administrateur.';
    } else {
        db()->prepare('DELETE FROM utilisateur WHERE id_u = ?')->execute([$cible]);
        header('Location: utilisateurs.php');
        exit;
    }
}

// Création / modification
if (isset($_POST['enregistrer'])) {
    $nom   = trim($_POST['nom_u'] ?? '');
    $email = trim($_POST['email_u'] ?? '');
    $role  = $_POST['role_u'] ?? '';
    $mdp   = $_POST['mdp_u'] ?? '';
    if ($id === $moi && $id) $role = 'admin';   // on ne peut pas se retirer ses propres droits

    if ($nom === '')                                $erreurs[] = 'Nom requis.';
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) $erreurs[] = 'Email invalide.';
    if (!in_array($role, ['client', 'admin'], true)) $erreurs[] = 'Rôle invalide.';
    if ($id && $role !== 'admin' && role_de($id) === 'admin' && nb_admins() <= 1) {
        $erreurs[] = 'Impossible de retirer le rôle du dernier administrateur.';
    }
    if (!$id && strlen($mdp) < 6)                  $erreurs[] = 'Mot de passe : 6 caractères minimum.';
    if ($id && $mdp !== '' && strlen($mdp) < 6)     $erreurs[] = 'Mot de passe : 6 caractères minimum (ou vide pour ne pas le changer).';

    if (!$erreurs) {
        try {
            if ($id) {
                db()->prepare('UPDATE utilisateur SET nom_u=?, email_u=?, role_u=? WHERE id_u=?')->execute([$nom, $email, $role, $id]);
                if ($mdp !== '') {
                    db()->prepare('UPDATE utilisateur SET mdp_u=? WHERE id_u=?')->execute([password_hash($mdp, PASSWORD_DEFAULT), $id]);
                }
            } else {
                db()->prepare('INSERT INTO utilisateur (nom_u, email_u, mdp_u, role_u) VALUES (?,?,?,?)')
                    ->execute([$nom, $email, password_hash($mdp, PASSWORD_DEFAULT), $role]);
            }
            header('Location: utilisateurs.php');
            exit;
        } catch (PDOException $ex) {
            if ($ex->getCode() !== '23000') throw $ex;
            $erreurs[] = 'Cet email est déjà utilisé.';
        }
    }
}

$st = db()->prepare('SELECT * FROM utilisateur WHERE id_u = ?');
$st->execute([$id]);
$edit = $id ? $st->fetch() : null;
$v = $edit ?: ['nom_u' => '', 'email_u' => '', 'role_u' => 'client'];
if (isset($_POST['enregistrer']) && $erreurs) $v = ['nom_u' => $nom, 'email_u' => $email, 'role_u' => $role];   // on garde la saisie
$nb_admins = nb_admins();
$users = db()->query('SELECT id_u, nom_u, email_u, role_u FROM utilisateur ORDER BY id_u DESC LIMIT 100')->fetchAll();

entete('Utilisateurs');
?>
<h1>Gestion des utilisateurs</h1>

<h2><?= $edit ? 'Modifier l\'utilisateur #' . $id : 'Ajouter un utilisateur' ?></h2>
<?php foreach ($erreurs as $err): ?><p class="form-error" role="alert"><?= e($err) ?></p><?php endforeach; ?>
<form method="post" class="product-form">
    <p><input name="nom_u" placeholder="Nom" required value="<?= e($v['nom_u']) ?>"></p>
    <p><input type="email" name="email_u" placeholder="Email" required value="<?= e($v['email_u']) ?>"></p>
    <p><input type="password" name="mdp_u" placeholder="<?= $edit ? 'Nouveau mot de passe (vide = inchangé)' : 'Mot de passe' ?>" <?= $edit ? '' : 'required' ?>></p>
    <p>
        <select name="role_u" <?= $id === $moi && $id ? 'disabled' : '' ?>>
            <?php foreach (['client', 'admin'] as $r): ?>
                <option <?= $v['role_u'] === $r ? 'selected' : '' ?>><?= $r ?></option>
            <?php endforeach; ?>
        </select>
    </p>
    <button name="enregistrer" value="1">Enregistrer</button>
    <?php if ($edit): ?><a href="utilisateurs.php">Annuler</a><?php endif; ?>
</form>

<h2>Utilisateurs</h2>
<div class="table-wrapper">
<table class="data-table admin-table">
    <tr><th>#</th><th>Nom</th><th>Email</th><th>Rôle</th><th></th></tr>
    <?php foreach ($users as $u): ?>
    <tr>
        <td><?= $u['id_u'] ?></td>
        <td><?= e($u['nom_u']) ?></td>
        <td><?= e($u['email_u']) ?></td>
        <td><?= e($u['role_u']) ?></td>
        <td>
            <a href="utilisateurs.php?id=<?= $u['id_u'] ?>">Modifier</a>
            <?php if ($u['id_u'] != $moi && !($u['role_u'] === 'admin' && $nb_admins <= 1)): ?>
            <form method="post" class="inline-form" onsubmit="return confirm('Supprimer ?')">
                <button name="supprimer" value="<?= $u['id_u'] ?>">Supprimer</button>
            </form>
            <?php endif; ?>
        </td>
    </tr>
    <?php endforeach; ?>
</table>
</div>
</main>
</body>
</html>
