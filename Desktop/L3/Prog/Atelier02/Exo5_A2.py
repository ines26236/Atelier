def rendu_monnaie_simple2(montant, valeurs, stock):
    rendu = []  

    for i in range(len(valeurs)):
        valeur = valeurs[i]
        dispo = stock[i]

        # calculer combien on peut rendre de cette valeur
        nb = min(montant // valeur, dispo)
        rendu.append(nb)

        # réduire le montant restant
        montant -= nb * valeur

    if montant > 0:
        print("Impossible de rendre exactement la monnaie avec le stock disponible.")
    return rendu


valeurs = [50, 20, 10, 5, 2, 1]
stock   = [2, 3, 5, 5, 5, 10]
montant = 87

print(rendu_monnaie_simple2(montant, valeurs, stock))
