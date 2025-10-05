def runGame():
    import random
    
    # Construire la liste des mots à partir du fichier
    lst = build_list("capitales.txt")
    
    # Tirage aléatoire
    mot = random.choice(lst)
    
    lpos = []
    erreurs = 0
    max_erreurs = 5
    
    print("Bienvenue au jeu du pendu !")
    print(outputStr(mot, lpos))
    
    while erreurs < max_erreurs and len(lpos) < len(mot):
        lettre = input("Entrez une lettre : ").lower()
        indices = places_lettre(lettre, mot)
        
        if indices:
            for i in indices:
                if i not in lpos:
                    lpos.append(i)
            print("Bien !")
        else:
            erreurs += 1
            print(f"Lettre incorrecte ! Erreurs : {erreurs}/{max_erreurs}")
        
        print(outputStr(mot, lpos))
        
        if erreurs == 1: print(C1)
        elif erreurs == 2: print(C2)
        elif erreurs == 3: print(C3)
        elif erreurs == 4: print(C4)
        elif erreurs == 5: print(C5)
    
    if len(lpos) == len(mot):
        print("Félicitations ! Vous avez trouvé le mot :", mot)
    else:
        print("Perdu ! Le mot était :", mot)
