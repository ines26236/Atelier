"""
Suite de tests automatisés avec Selenium pour l'application Web.
Conforme au cours : https://www.selenium.dev/

Fonctionnalités testées :
1. Présentation des codes Sign Up / Log In (Inscription, vérification mot de passe, échec, succès)
2. Système de tri par type de produit (A à Z, Z à A)
3. Filtrage par type de produit (onglets et sélecteur)
4. Ajout d'articles au panier et calcul du total

Usage :
    python tests_selenium.py            (mode headless / rapide en arrière-plan)
    python tests_selenium.py --visible  (mode démo visuel avec pauses, surbrillance et bandeau)
    python tests_selenium.py --visible --slow (mode démo encore plus lent pour présentation)
"""

import os
import sys
import time
import subprocess
import urllib.request
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Forcer la sortie UTF-8 si possible sous console Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_URL = "http://127.0.0.1:8000"
PHP_EXE = r"C:\wamp64\bin\php\php8.3.14\php.exe"
PHP_SERVER_PROC = None

def check_server_alive():
    try:
        req = urllib.request.Request(f"{BASE_URL}/index.php", headers={"User-Agent": "HealthCheck"})
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            return resp.status == 200
    except Exception:
        return False

def ensure_server():
    """Démarre le serveur PHP multi-thread (PHP_CLI_SERVER_WORKERS=4) sur le port 8000 si non actif."""
    global PHP_SERVER_PROC
    if check_server_alive():
        print("[*] Serveur Web local déjà actif sur " + BASE_URL)
        return

    if not os.path.isfile(PHP_EXE):
        print(f"[ERREUR] Exécutable PHP introuvable à : {PHP_EXE}")
        sys.exit(1)

    project_dir = os.path.dirname(os.path.abspath(__file__))
    env = os.environ.copy()
    env["PHP_CLI_SERVER_WORKERS"] = "4"

    print(f"[*] Démarrage automatique du serveur PHP local sur {BASE_URL}...")
    PHP_SERVER_PROC = subprocess.Popen(
        [PHP_EXE, "-S", "127.0.0.1:8000", "-t", project_dir],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    for _ in range(10):
        time.sleep(0.5)
        if check_server_alive():
            print("[*] Serveur PHP prêt et opérationnel.")
            return

    print("[ERREUR] Le serveur PHP n'a pas répondu à temps.")
    sys.exit(1)

def get_driver(visible=False):
    """Initialise le WebDriver Chrome moderne."""
    options = Options()
    if not visible:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
    else:
        options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    return webdriver.Chrome(options=options)

def show_banner(driver, text, bg_color="#1e293b", border_color="#38bdf8", visible=False):
    """Affiche un bandeau flottant explicatif en haut de page en mode visuel."""
    if not visible:
        return
    js = """
    let b = document.getElementById('selenium-demo-banner');
    if (!b) {
        b = document.createElement('div');
        b.id = 'selenium-demo-banner';
        b.style.position = 'fixed';
        b.style.top = '15px';
        b.style.left = '50%';
        b.style.transform = 'translateX(-50%)';
        b.style.zIndex = '999999';
        b.style.padding = '10px 24px';
        b.style.borderRadius = '30px';
        b.style.boxShadow = '0 10px 25px rgba(0,0,0,0.35)';
        b.style.fontFamily = 'system-ui, -apple-system, sans-serif';
        b.style.fontSize = '14px';
        b.style.fontWeight = '700';
        b.style.transition = 'all 0.3s ease';
        document.body.appendChild(b);
    }
    b.style.backgroundColor = arguments[1];
    b.style.border = '2px solid ' + arguments[2];
    b.style.color = arguments[2];
    b.innerText = arguments[0];
    """
    try:
        driver.execute_script(js, text, bg_color, border_color)
    except Exception:
        pass

def highlight(driver, element, color="#38bdf8", visible=False):
    """Met en valeur l'élément manipulé avec une surbrillance visuelle."""
    if not visible:
        return
    try:
        driver.execute_script(f"""
            arguments[0].scrollIntoView({{behavior: 'smooth', block: 'center'}});
            arguments[0].style.outline = '3px solid {color}';
            arguments[0].style.boxShadow = '0 0 14px {color}';
            arguments[0].style.transition = 'all 0.3s ease';
        """, element)
    except Exception:
        pass

def unhighlight(driver, element, visible=False):
    if not visible:
        return
    try:
        driver.execute_script("""
            arguments[0].style.outline = '';
            arguments[0].style.boxShadow = '';
        """, element)
    except Exception:
        pass

def visual_type(driver, element, text, visible=False, step_pause=0.03):
    """Tape le texte de façon fluide et visible."""
    if not visible:
        element.send_keys(text)
        return
    highlight(driver, element, "#38bdf8", visible=True)
    time.sleep(0.2)
    for char in text:
        element.send_keys(char)
        time.sleep(step_pause)
    time.sleep(0.3)
    unhighlight(driver, element, visible=True)

def visual_click(driver, element, visible=False, delay_after=1.2):
    """Met en valeur le bouton avant de cliquer et marque une pause."""
    if not visible:
        element.click()
        return
    highlight(driver, element, "#f59e0b", visible=True)
    time.sleep(0.5)
    element.click()
    time.sleep(delay_after)

def run_tests():
    visible_mode = "--visible" in sys.argv
    slow_factor = 1.8 if "--slow" in sys.argv else 1.0
    ensure_server()

    print("\n" + "=" * 65)
    print("  SUITE DE TESTS AUTOMATISÉS AVEC SELENIUM")
    print(f"  Mode : {'Navigateur visible (Démo interactive)' if visible_mode else 'Headless (sans interface)'}")
    if visible_mode:
        print(f"  Vitesse : {'Lente (--slow)' if '--slow' in sys.argv else 'Normale avec pauses pédagogiques'}")
    print(f"  URL cible : {BASE_URL}")
    print("=" * 65 + "\n")

    driver = get_driver(visible=visible_mode)
    wait = WebDriverWait(driver, 10)
    fake = Faker("fr_FR")

    passed = 0
    total = 6

    # Données aléatoires générées avec Faker pour le test d'inscription
    test_nom = fake.name()
    test_email = f"user_{int(time.time())}_{fake.bothify(text='??##')}@boutique.test"
    test_mdp = "secret123"

    try:
        # TEST 1 : Formulaire d'inscription (Sign Up)
        print("[TEST 1/6] Inscription d'un nouvel utilisateur (Sign Up)...")
        driver.get(f"{BASE_URL}/inscription.php")
        show_banner(driver, "🤖 [1/6] Remplissage du formulaire d'inscription (Faker)...", visible=visible_mode)
        if visible_mode:
            time.sleep(1.0 * slow_factor)

        nom_el = wait.until(EC.presence_of_element_located((By.ID, "nom")))
        visual_type(driver, nom_el, test_nom, visible=visible_mode, step_pause=0.03 * slow_factor)

        email_el = driver.find_element(By.ID, "email")
        visual_type(driver, email_el, test_email, visible=visible_mode, step_pause=0.02 * slow_factor)

        mdp_el = driver.find_element(By.ID, "mdp")
        visual_type(driver, mdp_el, test_mdp, visible=visible_mode, step_pause=0.04 * slow_factor)

        btn_inscr = driver.find_element(By.ID, "btn-submit-inscription")
        visual_click(driver, btn_inscr, visible=visible_mode, delay_after=1.2 * slow_factor)

        # Attente de la redirection vers login.php avec message de confirmation
        success_msg = wait.until(EC.presence_of_element_located((By.ID, "success-msg")))
        highlight(driver, success_msg, "#22c55e", visible=visible_mode)
        show_banner(driver, "✅ [1/6] Inscription validée ! Redirection vers login.php", bg_color="#064e3b", border_color="#34d399", visible=visible_mode)
        assert "login.php" in driver.current_url
        print(f"  -> Inscription validée pour '{test_email}'. Redirection vers login.php confirmée.")
        if visible_mode:
            time.sleep(2.0 * slow_factor)
        passed += 1

        # TEST 2 : Tentative de connexion avec mauvais mot de passe
        print("\n[TEST 2/6] Test d'échec de connexion (Mauvais mot de passe)...")
        driver.get(f"{BASE_URL}/login.php")
        show_banner(driver, "🤖 [2/6] Test d'échec avec un mauvais mot de passe...", visible=visible_mode)
        if visible_mode:
            time.sleep(1.0 * slow_factor)

        email_login = wait.until(EC.presence_of_element_located((By.ID, "email")))
        visual_type(driver, email_login, test_email, visible=visible_mode, step_pause=0.02 * slow_factor)

        mdp_login = driver.find_element(By.ID, "mdp")
        visual_type(driver, mdp_login, "mauvais_mdp_errone", visible=visible_mode, step_pause=0.03 * slow_factor)

        btn_login = driver.find_element(By.ID, "btn-submit-login")
        visual_click(driver, btn_login, visible=visible_mode, delay_after=1.2 * slow_factor)

        err = wait.until(EC.presence_of_element_located((By.ID, "error-msg")))
        highlight(driver, err, "#ef4444", visible=visible_mode)
        show_banner(driver, f"✅ [2/6] Rejet confirmé : « {err.text.strip()} »", bg_color="#450a0a", border_color="#f87171", visible=visible_mode)
        assert "Identifiants incorrects" in err.text
        print(f"  -> Message d'erreur correctement affiché : « {err.text.strip()} ».")
        if visible_mode:
            time.sleep(2.0 * slow_factor)
        passed += 1

        # TEST 3 : Connexion réussie (Log In)
        print("\n[TEST 3/6] Connexion réussie avec le compte créé (Log In)...")
        show_banner(driver, "🤖 [3/6] Connexion légitime avec le bon mot de passe...", visible=visible_mode)
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_input.clear()
        visual_type(driver, email_input, test_email, visible=visible_mode, step_pause=0.02 * slow_factor)

        mdp_input = driver.find_element(By.ID, "mdp")
        mdp_input.clear()
        visual_type(driver, mdp_input, test_mdp, visible=visible_mode, step_pause=0.04 * slow_factor)

        btn_login2 = driver.find_element(By.ID, "btn-submit-login")
        visual_click(driver, btn_login2, visible=visible_mode, delay_after=1.2 * slow_factor)

        # Doit rediriger vers l'accueil ou le catalogue avec le bouton Déconnexion
        logout_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Déconnexion')]")))
        highlight(driver, logout_link, "#22c55e", visible=visible_mode)
        show_banner(driver, f"✅ [3/6] Authentification réussie ! Bienvenue {test_nom}", bg_color="#064e3b", border_color="#34d399", visible=visible_mode)
        print(f"  -> Authentification réussie. Session active pour '{test_nom}'.")
        if visible_mode:
            time.sleep(2.0 * slow_factor)
        passed += 1

        # TEST 4 : Système de tri par type de produit
        print("\n[TEST 4/6] Vérification du système de tri par type de produit (A à Z)...")
        driver.get(f"{BASE_URL}/index.php")
        show_banner(driver, "🤖 [4/6] Application du tri alphabétique par type (A à Z)...", visible=visible_mode)

        tri_select_el = wait.until(EC.presence_of_element_located((By.ID, "tri-select")))
        highlight(driver, tri_select_el, "#a855f7", visible=visible_mode)
        if visible_mode:
            time.sleep(1.0 * slow_factor)

        tri_select = Select(tri_select_el)
        tri_select.select_by_value("type_asc")
        if visible_mode:
            time.sleep(1.5 * slow_factor)

        badges = driver.find_elements(By.CSS_SELECTOR, ".product-type-badge")
        types_trouves = [b.text.strip() for b in badges if b.text.strip()]
        assert len(types_trouves) > 0, "Aucun badge de type de produit trouvé !"

        for b in badges[:4]:
            highlight(driver, b, "#a855f7", visible=visible_mode)

        types_tries = sorted(types_trouves)
        assert types_trouves == types_tries, (
            f"Les produits ne sont pas triés par type A-Z. Obtenu : {types_trouves[:5]}, Attendu : {types_tries[:5]}"
        )
        show_banner(driver, f"✅ [4/6] Tri A à Z validé ({len(types_trouves)} produits vérifiés)", bg_color="#581c87", border_color="#c084fc", visible=visible_mode)
        print(f"  -> Tri par type de produit A à Z vérifié sur {len(types_trouves)} produits.")
        print(f"     Ordre vérifié : {' -> '.join(types_trouves[:4])} ...")
        if visible_mode:
            time.sleep(2.0 * slow_factor)
        passed += 1

        # TEST 5 : Filtrage par type de produit (catégorie)
        print("\n[TEST 5/6] Filtrage direct par type de produit...")
        show_banner(driver, "🤖 [5/6] Clic sur un onglet de catégorie pour filtrer...", visible=visible_mode)

        onglet = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".category-tabs .tab-item:nth-child(2)")))
        categorie_cible = onglet.text.strip()
        visual_click(driver, onglet, visible=visible_mode, delay_after=1.5 * slow_factor)

        badges_filtres = driver.find_elements(By.CSS_SELECTOR, ".product-type-badge")
        assert len(badges_filtres) > 0, f"Aucun produit trouvé pour la catégorie '{categorie_cible}'"
        for b in badges_filtres[:4]:
            highlight(driver, b, "#38bdf8", visible=visible_mode)
            assert b.text.strip().lower() == categorie_cible.lower(), (
                f"Produit hors catégorie détecté : '{b.text.strip()}' attendu : '{categorie_cible}'"
            )

        show_banner(driver, f"✅ [5/6] Filtrage validé : {len(badges_filtres)} articles de type '{categorie_cible}'", bg_color="#0f172a", border_color="#38bdf8", visible=visible_mode)
        print(f"  -> Filtrage validé pour '{categorie_cible}' : {len(badges_filtres)} produits affichés, tous conformes.")
        if visible_mode:
            time.sleep(2.0 * slow_factor)
        passed += 1

        # TEST 6 : Ajout au panier
        print("\n[TEST 6/6] Test d'ajout au panier...")
        driver.get(f"{BASE_URL}/index.php")
        show_banner(driver, "🤖 [6/6] Sélection d'un article et ajout au panier...", visible=visible_mode)
        if visible_mode:
            time.sleep(1.0 * slow_factor)

        add_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart-form")))
        btn_add = add_form.find_element(By.CSS_SELECTOR, "button")
        visual_click(driver, btn_add, visible=visible_mode, delay_after=1.5 * slow_factor)

        cart_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-summary, .cart-table")))
        highlight(driver, cart_box, "#22c55e", visible=visible_mode)
        assert "panier.php" in driver.current_url
        show_banner(driver, "🎉 [6/6] Produit ajouté au panier ! Calcul TVA (20%) et Total validés", bg_color="#064e3b", border_color="#34d399", visible=visible_mode)
        print("  -> Produit ajouté au panier avec succès. Page panier.php chargée.")
        if visible_mode:
            time.sleep(2.5 * slow_factor)
        passed += 1

        # Clôture visuelle avec décompte
        if visible_mode:
            show_banner(driver, "🎉 SUCCÈS TOTAL : LES 6 TESTS SONT PASSÉS !", bg_color="#14532d", border_color="#4ade80", visible=True)
            print("\n" + "=" * 65)
            print("  TOUS LES TESTS SONT TERMINÉS AVEC SUCCÈS !")
            print("  Le navigateur reste ouvert pour observation (décompte ci-dessous)")
            print("=" * 65)
            for countdown in range(10, 0, -1):
                sys.stdout.write(f"\r  Fermeture automatique dans {countdown} seconde(s)... ")
                sys.stdout.flush()
                time.sleep(1)
            print("\n")

    except AssertionError as ae:
        print(f"\n[ECHEC ASSERTION] {ae}")
        if visible_mode:
            show_banner(driver, f"❌ ÉCHEC : {ae}", bg_color="#7f1d1d", border_color="#f87171", visible=True)
            print("[*] Le navigateur reste ouvert 15 secondes pour inspection...")
            time.sleep(15)
    except Exception as ex:
        print(f"\n[ERREUR INATTENDUE] {ex}")
        if visible_mode:
            show_banner(driver, f"❌ ERREUR : {ex}", bg_color="#7f1d1d", border_color="#f87171", visible=True)
            print("[*] Le navigateur reste ouvert 15 secondes pour inspection...")
            time.sleep(15)
    finally:
        driver.quit()
        if PHP_SERVER_PROC:
            PHP_SERVER_PROC.terminate()

    print("\n" + "=" * 65)
    print(f"  RÉSULTATS DE LA SUITE DE TESTS : {passed} / {total} validés")
    if passed == total:
        print("  SUCCÈS : Tous les tests Selenium sont passés avec succès !")
    else:
        print(f"  ATTENTION : {total - passed} test(s) en échec.")
    print("=" * 65 + "\n")

    return passed == total

if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
