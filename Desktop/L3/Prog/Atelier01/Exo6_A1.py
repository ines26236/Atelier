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


revenu = 25000
print(f"Pour un revenu de {revenu}€, l'impôt est : {calculer_mes_impots(revenu)}€")
