def ouvrante(car: str) -> bool:
    return car in "([{"
def fermante(car: str) -> bool:
    return car in ")]}"
def renverse(car: str) -> str:
    mapping = {')':'(', ']':'[', '}':'{'}
    if car in mapping:
        return mapping[car]
    else:
        return car
def operateur(car: str) -> bool:
    return car in "+-*"
def nombre(car: str) -> bool:
    return car.isdigit()
def caractere_valide(car: str) -> bool:
    return ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or car == " "
def verif_parenthese(expression: str) -> bool:
    # Vérification des caractères valides
    for car in expression:
        if not caractere_valide(car):
            return False

    # Pile pour vérifier la parenthésage
    P = []
    for car in expression:
        if ouvrante(car):
            P.append(car)  # empiler
        elif fermante(car):
            if len(P) == 0:  # pile vide mais fermante
                return False
            if P[-1] == renverse(car):  # correspond à la dernière ouvrante
                P.pop()
            else:
                return False
    # Si la pile est vide à la fin, toutes les parenthèses sont équilibrées
    return len(P) == 0


print(renverse(')'))  
print(ouvrante(')'))  
print(fermante('['))  
print(operateur('*'))
print(nombre('a'))
print(caractere_valide('+*-]'))

print(verif_parenthese("(3+2) * 6-1"))  
print(verif_parenthese("((3+2)*6-1"))   
print(verif_parenthese("(5+7]*12"))     
 




