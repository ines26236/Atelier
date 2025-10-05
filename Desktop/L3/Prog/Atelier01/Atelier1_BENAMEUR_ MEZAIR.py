
#Exercice1
def message_imc(imc: float) -> str:
    if imc < 16.5:
        return "dénutrition ou famine"
    elif 16.5 <= imc < 18.5:
        return "maigreur"
    elif 18.5 <= imc < 25:
        return "corpulence normale"
    elif 25 <= imc < 30:
        return "surpoids"
    elif 30 <= imc < 35:
        return "obésité modérée"
    elif 35 <= imc < 40:
        return "obésité sévère"
    else:
        return "obésité morbide"


poids = float(input("Entrez votre poids en kg : "))
taille = float(input("Entrez votre taille en m : "))

# Formule IMC = poids / (taille²)
imc = poids / (taille ** 2)

print(f"Votre IMC est {imc:.2f}")
print("Interprétation :", message_imc(imc))

#Exercice2 
def est_bissextile(annee: int) -> bool:
   
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

annee = int(input("Entrez une année : "))

if est_bissextile(annee):
    print(f"{annee} est une année bissextile ")
else:
    print(f"{annee} n'est pas une année bissextile ")

#Exercice3:
import math

def distance_3d(xA, yA, zA, xB, yB, zB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2 + (zB - zA)**2)

xA, yA, zA = 1, 2, 3
xB, yB, zB = 4, 6, 8

d = distance_3d(xA, yA, zA, xB, yB, zB)
print("La distance est :", round(d, 2))

#Exercice4:
def est_triangle(a: float, b: float, c: float) -> bool:
    
    return (a + b > c) and (a + c > b) and (b + c > a)

a = float(input("Longueur a : "))
b = float(input("Longueur b: "))
c = float(input("Longueur c: "))

if est_triangle(a, b, c):
    print("Ces segments peuvent former un triangle ")
else:
    print("Ces segments ne peuvent pas former un triangle ")

#Exercice 5:
def conversion_masse(valeur, unite_depart, unite_arrivee):
   
    if unite_depart == "kg" and unite_arrivee == "g":
        return valeur * 1000
    elif unite_depart == "g" and unite_arrivee == "kg":
        return valeur / 1000
    else:
        return valeur  # si les unités sont les mêmes


# Exemple d’utilisation
print(conversion_masse(45, "kg", "g"))   # 45000
print(conversion_masse(2000, "g", "kg")) # 2
print(conversion_masse(5, "kg", "kg"))   # 5

#Exercice 6:
####### Exercice6 Amélioré par l'IA :
#prompt: Donner moi l'amélioration plus clair avec des explications pour optimiser  ce code

from typing import Union

# Tranches fiscales : (plafond, taux)
TRANCHES = [
    (11498, 0.0),    # Pas d'impôt jusqu'à 11498 €
    (29315, 0.11),
    (83823, 0.30),
    (180294, 0.41),
    (float('inf'), 0.45)  # Tout ce qui dépasse 180294 € (infini+)
]

def calculer_mes_impots(revenu: float) -> float:
   
    impot = 0.0
    revenu_precedent = 0.0

    for plafond, taux in TRANCHES:
        if revenu > revenu_precedent:
            montant_tranche = min(revenu, plafond) - revenu_precedent
            impot += montant_tranche * taux
            revenu_precedent = plafond
        else:
            break

    return round(impot, 2)


# Exemple d’utilisation
revenu = 25000
print(f"Pour un revenu de {revenu}€, l'impôt est : {calculer_mes_impots(revenu)}€")

