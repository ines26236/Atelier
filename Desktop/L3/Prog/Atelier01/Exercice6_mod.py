""" EXERCICE 6 """
from typing import Union
def CalcumerMesImpots(MonRevenu:float)-> Union[float, str]:
    """
    Calcule le montant des impôts à payer en fonction du revenu annuel selon les tranches fiscales.
    
    Paramètre :
    - MonRevenu (int) : le revenu annuel en euros.
    
    Retour :
    - float ou str : montant des impôts à payer ou message indiquant qu'aucun impôt n'est dû.
    """

    if MonRevenu>=11498 and MonRevenu <= 29315 :
        return MonRevenu*0.11
    elif MonRevenu>=29316 and MonRevenu <= 83823 :
        return MonRevenu*0.30
    elif MonRevenu>=83824 and MonRevenu <= 180294 :
        return MonRevenu*0.41
    elif MonRevenu>180294  :
        return MonRevenu*0.45
    else :
        return "Pas d'impot a reverser"

dictionnaireimpot={'tranche1':1959.87,'tranche2':16352.1,
                   'tranche3':39552.7}

def calculimpotv2(monrevenu:float )->Union [float,str]:
    if monrevenu>=11498 and monrevenu <= 29315 :
        return (monrevenu-11498)*0.11
    elif monrevenu>=29316 and monrevenu <= 83823 :
        return ((monrevenu-29316)*0.30) + dictionnaireimpot['tranche1']
    elif monrevenu>=83824 and monrevenu <= 180294 :
        return ((monrevenu-83824)*0.41)+ dictionnaireimpot['tranche1']+ dictionnaireimpot['tranche2']
    elif monrevenu>180294  :
        return ((monrevenu-180294)*0.45) + dictionnaireimpot['tranche1']+ dictionnaireimpot['tranche2']+ dictionnaireimpot['tranche3']
    else :
        return "Pas d'impot a reverser"

print (CalcumerMesImpots(25000))
print (calculimpotv2(25000))



########## Exercice Amélioré par l'IA

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
