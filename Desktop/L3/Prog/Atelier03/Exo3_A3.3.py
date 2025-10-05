import random
from outputStr import outputStr
from places_lettre import places_lettre

def runGame():
    lst = ['paris','londres','madrid','berlin','new-york']
    mot = random.choice(lst)
    lpos = []
    erreurs = 0
    max_erreurs = 5
    print("Bienvenue au jeu du pendu !")
    print("Le mot à deviner :")
    print(outputStr(mot, lpos))
    while erreurs < max_erreurs and len(lpos) < len(mot):
        lettre = input("Entrez une lettre : ")
        
        # Vérifier si la lettre est dans le mot
        indices = places_lettre(lettre, mot)
        
        if indices:
            # Ajouter les indices trouvés
            for i in indices:
                if i not in lpos:
                    lpos.append(i)
            print("Bien !")
        else:
            erreurs += 1
            print(f"Lettre incorrecte ! Erreurs : {erreurs}/{max_erreurs}")
        
        # Affichage du mot actuel
        print(outputStr(mot, lpos))
        
        # Affichage du pendu selon le nombre d'erreurs
        if erreurs == 1:
            print(C1)
        elif erreurs == 2:
            print(C2)
        elif erreurs == 3:
            print(C3)
        elif erreurs == 4:
            print(C4)
        elif erreurs == 5:
            print(C5)
    
    # Fin de jeu
    if len(lpos) == len(mot):
        print("Félicitations ! Vous avez trouvé le mot :", mot)
    else:
        print("Perdu ! Le mot était :", mot) 
runGame()