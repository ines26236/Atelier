def mots_Nlettres(lst_mot, n):
     return [mot for mot in lst_mot if len(mot) == n]

def commence_par(mot, prefixe):
    return mot.startswith(prefixe)

def finit_par(mot, suffixe):
  return mot.endswith(suffixe)

def finissent_par(lst_mot, suffixe):
    return [mot for mot in lst_mot if mot.endswith(suffixe)]

def commencent_par(lst_mot, prefixe):
    return [mot for mot in lst_mot if mot.startswith(prefixe)]

def liste_mots(lst_mot, prefixe, suffixe, n):
    return [mot for mot in lst_mot if mot.startswith(prefixe) and mot.endswith(suffixe) and len(mot) == n]

def dictionnaire(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        return [ligne.strip() for ligne in f.readlines()]

#  Tests 

def test_exercice():
    lst_mot = ["jouer","bonjour","punir","jour","aurevoir","revoir",
               "pouvoir","cour","abajour","finir","aimer"]

    print("== Test mots_Nlettres ==")
    print("Mots de 4 lettres :", mots_Nlettres(lst_mot, 4))
    print("Mots de 5 lettres :", mots_Nlettres(lst_mot, 5))

    print("\n== Test commence_par ==")
    print("'bonjour' commence par 'bon' ?", commence_par("bonjour", "bon"))
    print("'jour' commence par 'bon' ?", commence_par("jour", "bon"))

    print("\n== Test finit_par ==")
    print("'revoir' finit par 'voir' ?", finit_par("revoir", "voir"))
    print("'cour' finit par 'voir' ?", finit_par("cour", "voir"))

    print("\n== Test finissent_par ==")
    print("Mots qui finissent par 'ir' :", finissent_par(lst_mot, "ir"))
    print("Mots qui finissent par 'our' :", finissent_par(lst_mot, "our"))

    print("\n== Test liste_mots ==")
    print("Mots commençant par 'p', finissant par 'ir', longueur 5 :", liste_mots(lst_mot, "p", "ir", 5))
    print("Mots commençant par 'a', finissant par 'r', longueur 8 :", liste_mots(lst_mot, "a", "r", 8))

    print("\n== Test dictionnaire ==")
    fichier = "C:\\Users\\Utilisateur\\Desktop\\L3\\Prog\\littre.txt" 
    mots_fichier = dictionnaire(fichier)
    print("Premiers mots du fichier :", mots_fichier[:10])  

    print("\n== Test combinaison dictionnaire + liste_mots ==")
    result = liste_mots(mots_fichier, "p", "ir", 5)
    print("Mots du fichier commençant par 'p', finissant par 'ir', longueur 5 :", result)



if __name__ == "__main__":
    test_exercice()
