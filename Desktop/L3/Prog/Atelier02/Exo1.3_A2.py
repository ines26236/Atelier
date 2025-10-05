def moyenne_sup(ma_liste: list, elt: int) -> float:
    somme = 0
    compteur = 0
    for x in ma_liste:
        if x > elt:
            somme += x
            compteur += 1
    if compteur == 0:
        return 0
    return somme / compteur
liste = [1, 5, 8, 3, 10, 2]
elt = 4

print("Moyenne des valeurs supérieures à", elt, ":", moyenne_sup(liste, elt))
