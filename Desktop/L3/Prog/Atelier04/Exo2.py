import random

def mix_list(list_to_mix):
    copie_list = list_to_mix[:]
    mixed = []
    
    while copie_list:
        # On choisit un indice aléatoire 
        index = random.randint(0, len(copie_list) - 1)
        
        element = copie_list.pop(index)
        mixed.append(element)
    
    return mixed
# Test de votre code
lst_sorted = [i for i in range(10)]

print(lst_sorted)
print('Liste triée de départ :', lst_sorted)

mixed_list = mix_list(lst_sorted)

print('Liste mélangée obtenue :', mixed_list)
print("Liste triée de départ après appel à mix_list, elle doit être inchangée :", lst_sorted)

# assert permet de vérifier qu'une condition est vraie
assert lst_sorted != mixed_list

