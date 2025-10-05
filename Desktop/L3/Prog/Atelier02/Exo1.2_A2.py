def nb_sup_index(ma_liste: list, element: int) -> int:
    compteur = 0
    for i in range(len(ma_liste)):   # on parcourt les indices
        if ma_liste[i] > element:
            compteur += 1
    return compteur

liste = [2, 15, 17,0,4, 10, 2]

print(nb_sup_index(liste, 8))
#avec boucle while

def nb_sup_while(ma_liste:list, element : int)->list:
    liste=[]
    i=0
    while i < len(ma_liste):
        if ma_liste[i]> element:
            liste.append(ma_liste[i])
        i+=1

    return liste
L = [1, 2, 3, 5]
print("Nombre d'éléments supérieurs à 3 :", nb_sup_while(L, 5))
