def dictionnaire(fichier):

    with open(fichier, "r", encoding="utf-8") as f:
        return [ligne.strip() for ligne in f.readlines()]
    


fichier = "C:\\Users\\Utilisateur\\Desktop\\L3\\Prog\\littre.txt" 
mots_fichier = dictionnaire(fichier)
print("Les mots du fichier :", mots_fichier[1:])  


