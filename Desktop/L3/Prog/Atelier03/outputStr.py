def outputStr( mot:str, lpos:list) -> str:
    resultat = []
    for i, lettre in enumerate(mot):
        if i in lpos:
            resultat.append(lettre)
        else:
            resultat.append('_')
    
        return ''.join(resultat)
     
  
print(outputStr('bonjour', [0,1,3]))      


