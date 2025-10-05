def agencement(nbEmplacements: int, lObjets: list):
    v1, v2 = [], []
    
    for obj in lObjets:
        if obj not in v1 and len(v1) < nbEmplacements:
            v1.append(obj)
        elif obj not in v2 and len(v2) < nbEmplacements:
            v2.append(obj)
        else:
            return None  
    
    return v1, v2
nbEmplacements = 5
lObjets = [1, 2, 2, 3, 4, 5,5,6]

solution = agencement(nbEmplacements, lObjets)
print(solution)
