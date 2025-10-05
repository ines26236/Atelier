def ind_max(lst: list) -> int:
    if not lst:   
        return 0  
    
    indice_max = 0        
    maximum = lst[0]
    
    for i in range(1, len(lst)):  
        if lst[i] > maximum:
            maximum = lst[i]
            indice_max = i
    return indice_max
liste = [3, 7, 2, 10, 5]
print("Indice du max :", ind_max(liste))