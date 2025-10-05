def mot_correspond(mot: str, motif: str) -> bool:
    if len(mot) != len(motif):
        return False
    for i in range(len(mot)):
        if motif[i] != '.' and mot[i] != motif[i]:
            return False
    return True


print(mot_correspond("tarte", "t..t."))  # True
print(mot_correspond("cheval", "c..v..l"))  # False
print(mot_correspond("cheval", "c..v.l"))   # True

#----------fct2
def presente(lettre: str, mot: str) -> int:
    for i in range(len(mot)):
        if mot[i] == lettre:
            return i
    return -1



print(presente("a", "cheval"))  
print(presente("z", "cheval"))  #
#----------fct3

def mot_possible(mot: str, lettres: str) -> bool:
    lettres_dispo = list(lettres)  # on transforme en liste pour retirer les lettres utilisées
    for l in mot:
        idx = presente(l, ''.join(lettres_dispo))
        if idx == -1:
            return False
        else:
            # retirer la lettre utilisée
            lettres_dispo.pop(idx)
    return True

print(mot_possible("lapin", "abilnpq"))       # True
print(mot_possible("cheval", "abilnpq"))     # False
print(mot_possible("chapeau", "abcehpuv"))   # False
print(mot_possible("chapeau", "abcehpuva"))  # True

#--------------fct4
def mots_Nlettres(dico: list, n: int) -> list:
    """Retourne la liste des mots de longueur n dans dico"""
    return [mot for mot in dico if len(mot) == n]

def mot_optimaux(dico: list, lettres: str) -> list:
    longueur_max = len(lettres)
    for n in range(longueur_max, 0, -1):
        mots_n = mots_Nlettres(dico, n)
        possibles = [mot for mot in mots_n if mot_possible(mot, lettres)]
        if possibles:
            return possibles
    return []

# Exemple
dico = ["lapin", "cheval", "chapeau", "table", "piano", "avion"]
lettres = "abcehpuvli"
print(mot_optimaux(dico, lettres))  # ['chapeau']

