import random

def choose_element_list(list_in_which_to_choose):
   
    if not list_in_which_to_choose:
        return None  
    idx = random.randint(0, len(list_in_which_to_choose) - 1)
    return list_in_which_to_choose[idx]

# --- Test de la fonction ---
lst_sorted = [i for i in range(10)]
print('Liste triée de départ :', lst_sorted)

e1 = choose_element_list(lst_sorted)
print('À la première exécution,', e1, 'a été sélectionné')

e2 = choose_element_list(lst_sorted)
print('À la deuxième exécution,', e2, 'a été sélectionné')


# Vérification que deux éléments peuvent être différents (mais aléatoire)
if len(lst_sorted) > 1:
    assert e1 != e2