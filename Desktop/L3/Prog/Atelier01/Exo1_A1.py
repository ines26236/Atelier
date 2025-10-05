def message_imc(imc: float) -> str:
    if imc < 16.5:
        return "dénutrition ou famine"
    elif 16.5 <= imc < 18.5:
        return "maigreur"
    elif 18.5 <= imc < 25:
        return "corpulence normale"
    elif 25 <= imc < 30:
        return "surpoids"
    elif 30 <= imc < 35:
        return "obésité modérée"
    elif 35 <= imc < 40:
        return "obésité sévère"
    else:
        return "obésité morbide"


poids = float(input("Entrez votre poids en kg : "))
taille = float(input("Entrez votre taille en m : "))

# Formule IMC 
imc = poids / (taille ** 2)

print(f"Votre IMC est {imc:.2f}")
print("Interprétation :", message_imc(imc))
