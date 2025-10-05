def position_for(lst: list, elt: int) -> int:
    for i in range(len(lst)):
        if lst[i] == elt:
            return i
    return -1

def position_while(lst: list, elt: int) -> int:
    i = 0
    while i < len(lst):
        if lst[i] == elt:
            return i
        i += 1
    return -1
def nb_occurrences(lst: list, e: int) -> int:
    
    compteur = 0
    for x in lst:
        if x == e:
            compteur += 1
    return compteur
liste = [4, 7, 2, 9, 5,2,6,2]

print("la position pour la boucle for de 9 est: ",position_for(liste, 9)) 
print("La position pour la boucle while de 5 est : ",position_while(liste,5))
print("Le nombre d'occurrences de 2 est : ",nb_occurrences(liste,2))
