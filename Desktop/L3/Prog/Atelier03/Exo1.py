def full_name(str_arg: str) -> str:
    nom, prenom = str_arg.split()
    nom = nom.upper()
    prenom = prenom.capitalize()
    
   
    return f"{nom} {prenom}"

str_variable2test = "benameur iness"
print(full_name(str_variable2test))  
