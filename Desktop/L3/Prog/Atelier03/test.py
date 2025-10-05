def places_lettre(ch: str, mot: str) -> list:
   
    indices = []
    for i, lettre in enumerate(mot):
        if lettre == ch:
            indices.append(i)
    return indices

def test():
   mot = input("Entrez un mot : ").lower()  # On met en minuscules pour standardiser
   ch = input("Entrez une lettre à chercher : ").lower()
    
   result = places_lettre(ch, mot) 
   if result:
        print(f"La lettre '{ch}' se trouve aux positions : {result}")
   else:
        print(f"La lettre '{ch}' n'est pas dans le mot.")

