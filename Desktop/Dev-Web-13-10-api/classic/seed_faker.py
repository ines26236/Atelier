"""
Génération de données aléatoires avec Faker (Python)
Conforme au tutoriel : https://www.docstring.fr/blog/generer-des-donnees-aleatoires-avec-faker/

Usage :
    python seed_faker.py [nombre_de_produits]
    Exemple : python seed_faker.py 60
"""

import sys
import json
import random
from pathlib import Path
from faker import Faker
import pymysql

# Configuration de la base de données
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "2026_m1",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}

# Modèles réalistes par catégorie pour un catalogue high-tech cohérent
CATALOG_TEMPLATES = {
    "Smartphone": [
        "iPhone 15 Pro Max {spec}", "Samsung Galaxy S24 Ultra {spec}", "Google Pixel 8 Pro {spec}",
        "Xiaomi 14 Ultra {spec}", "OnePlus 12 {spec}", "Nothing Phone (2) {spec}"
    ],
    "Ordinateur portable": [
        "MacBook Pro M3 {spec}", "Dell XPS 15 {spec}", "Lenovo ThinkPad X1 Carbon {spec}",
        "Asus ZenBook Duo {spec}", "HP Spectre x360 {spec}", "Razer Blade 16 {spec}"
    ],
    "Casque audio": [
        "Sony WH-1000XM5 {spec}", "Bose QuietComfort Ultra {spec}", "Sennheiser Momentum 4 {spec}",
        "Apple AirPods Max {spec}", "JBL Tour One M2 {spec}", "Marshall Major IV {spec}"
    ],
    "Montre connectée": [
        "Apple Watch Series 9 {spec}", "Garmin Fenix 7 Pro {spec}", "Samsung Galaxy Watch 6 {spec}",
        "Pixel Watch 2 {spec}", "Huawei Watch GT 4 {spec}", "Withings ScanWatch 2 {spec}"
    ],
    "Tablette": [
        "iPad Pro 12.9 M2 {spec}", "Samsung Galaxy Tab S9 Ultra {spec}", "Microsoft Surface Pro 9 {spec}",
        "iPad Air 10.9 {spec}", "Lenovo Tab P12 Pro {spec}", "Xiaomi Pad 6 Max {spec}"
    ],
    "Caméra": [
        "Sony Alpha 7 IV {spec}", "Canon EOS R6 Mark II {spec}", "Fujifilm X-T5 {spec}",
        "Nikon Z6 II {spec}", "GoPro Hero 12 Black {spec}", "DJI Osmo Pocket 3 {spec}"
    ]
}

SPECS = ["128 Go", "256 Go", "512 Go", "1 To", "Édition Titane", "Sans fil ANC", "OLED 4K", "WiFi + 5G", "Noir Sidéral"]

PRICE_RANGES = {
    "Smartphone": (350.0, 1499.0),
    "Ordinateur portable": (599.0, 2899.0),
    "Casque audio": (79.0, 499.0),
    "Montre connectée": (149.0, 899.0),
    "Tablette": (299.0, 1399.0),
    "Caméra": (399.0, 2499.0)
}

def load_categories():
    cat_file = Path(__file__).parent / "categories.json"
    if cat_file.exists():
        try:
            with open(cat_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [c["categorie"] for c in data if "categorie" in c]
        except Exception:
            pass
    return list(CATALOG_TEMPLATES.keys())

def generate_product_name(fake: Faker, category: str) -> str:
    templates = CATALOG_TEMPLATES.get(category)
    if templates:
        template = random.choice(templates)
        spec = random.choice(SPECS)
        return template.format(spec=spec)
    # Fallback générique avec Faker
    return f"{category} {fake.company()} {fake.bothify(text='??-###').upper()}"

def seed(nb_produits: int = 60):
    if sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print(f"[*] Initialisation de Faker (fr_FR) et connexion MySQL...")
    fake = Faker("fr_FR")
    categories = load_categories()

    try:
        conn = pymysql.connect(**DB_CONFIG)
    except Exception as e:
        print(f"[ERREUR] Connexion MySQL impossible : {e}")
        print("Vérifiez que Wamp/MySQL est bien démarré sur le port 3306.")
        return False

    with conn.cursor() as cur:
        # 1. Comptes de test (Admin et Client)
        print("[*] Verification / creation des comptes utilisateurs...")
        admin_hash = "$2y$10$dsLR4XcKnvSVjX8SgMwP7uMgbNw9JVoBr9G3IKG2q1MRwN38/4zUi"
        client_hash = "$2y$10$EB36oi.Rzkdz6MB5L9NJH..lDOijVgLZ7FkECDAJDESDmsYjLq5Q6"

        cur.execute(
            """INSERT INTO utilisateur (nom_u, email_u, mdp_u, role_u)
               VALUES (%s, %s, %s, %s)
               ON DUPLICATE KEY UPDATE nom_u = VALUES(nom_u), role_u = VALUES(role_u)""",
            ("Administrateur", "admin@boutique.test", admin_hash, "admin")
        )
        cur.execute(
            """INSERT INTO utilisateur (nom_u, email_u, mdp_u, role_u)
               VALUES (%s, %s, %s, %s)
               ON DUPLICATE KEY UPDATE nom_u = VALUES(nom_u), role_u = VALUES(role_u)""",
            ("Client Test", "client@boutique.test", client_hash, "client")
        )

        # 2. Nombre de produits
        cur.execute("SELECT COUNT(*) AS total FROM produit")
        existing = cur.fetchone()["total"]
        print(f"[*] Produits actuellement en base : {existing}")

        print(f"[*] Generation de {nb_produits} produits avec Faker...")
        insert_sql = """
            INSERT INTO produit (type_p, designation_p, prix_ht, ppromo, date_in, stock_p)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        created = 0
        for _ in range(nb_produits):
            cat = random.choice(categories)
            name = generate_product_name(fake, cat)
            min_p, max_p = PRICE_RANGES.get(cat, (30.0, 999.0))
            prix_ht = round(random.uniform(min_p, max_p), 2)
            ppromo = random.choice([5, 10, 15, 20, 25, 30, 40, 50]) if random.random() < 0.28 else None
            date_in = fake.date_between(start_date="-1y", end_date="today")
            stock = 0 if random.random() < 0.08 else random.randint(3, 85)

            cur.execute(insert_sql, (cat, name, prix_ht, ppromo, date_in, stock))
            created += 1

        conn.commit()

        cur.execute("SELECT COUNT(*) AS total FROM produit")
        total_apres = cur.fetchone()["total"]

        print(f"[SUCCES] {created} produits crees avec succes !")
        print(f"[*] Total de produits dans la base : {total_apres}")
        print("\nComptes de test disponibles :")
        print("  - Admin  : admin@boutique.test / admin123")
        print("  - Client : client@boutique.test / client123")
        print("  - Categories : " + ", ".join(categories))

    conn.close()
    return True

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    seed(count)
