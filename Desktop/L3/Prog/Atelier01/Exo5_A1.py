def conversion_masse(valeur, unite_depart, unite_arrivee):
   
    if unite_depart == "kg" and unite_arrivee == "g":
        return valeur * 1000
    elif unite_depart == "g" and unite_arrivee == "kg":
        return valeur / 1000
    else:
        return valeur  # si les unités sont les mêmes

print(conversion_masse(45, "kg", "g"))  
print(conversion_masse(2000, "g", "kg"))
print(conversion_masse(5, "kg", "kg"))   
