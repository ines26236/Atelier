def val_max(lst: list) -> float:
    if not lst:   
        return 0
    maximum = lst[0]      
    for x in lst:        
        if x > maximum:  
            maximum = x
    return maximum
liste = [3, 7, 2, 10, 225]
print("Valeur maximale :", val_max(liste))  