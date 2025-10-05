def eval_horner(coeffs, x):
   
    resultat = 0
    for a in reversed(coeffs):
        resultat = resultat * x + a
    return resultat
print(eval_horner([1, 3, 2], 4))  
