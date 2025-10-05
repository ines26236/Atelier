def runGame():
    import random
    
    # Construire la liste des mots
    lst = build_list("capitales.txt")
    
    # Construire le dictionnaire {taille: [mots]}
    dico_mots = build_dict(lst)
    
    # Choix du niveau
    print("Choisissez un niveau : easy, normal, hard")
    niveau = input("Votre choix : ").lower()
    
    if niveau == "easy":
        tailles_possibles = [t for t in dico_mots.keys() if t < 7]
    elif niveau == "normal":
        tailles_possibles = [t for t in dico_mots.keys() if 6 < t < 9]
    elif niveau == "hard":
        tailles_possibles = [t for t in dico_mots.keys() if t > 8]
    else:
        print("Niveau invalide, niveau normal choisi par défaut.")
        tailles_possibles = [t for t in dico_mots.keys() if 6 < t < 9]
    
    # Choisir aléatoirement une taille parmi celles possibles
    word_len = random.choice(tailles_possibles)
    
    # Sélectionner un mot
    mot = select_word(dico_mots, word_len)
    
    # Initialisation du jeu
    lpos = []
    erreurs = 0
    max_erreurs = 5
    
    print("Bienvenue au jeu du pendu !")
    print("Le mot à deviner :")
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
