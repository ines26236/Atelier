import random

def extract_elements_list(list_in_which_to_choose, int_nbr_of_element_to_extract):    
    original_copy = list(list_in_which_to_choose)
    extracted = []

    for i in range(int_nbr_of_element_to_extract):
        idx = random.randint(0, len(original_copy) - 1)
        extracted.append(original_copy.pop(idx))
    
    return extracted

# --- Test de la fonction ---
lst_sorted = [i for i in range(10)]
print('Liste de départ :', lst_sorted)

sublist = extract_elements_list(lst_sorted, 5)
print('La sous-liste extraite est :', sublist)
print('Liste de départ après appel de la fonction :', lst_sorted)

