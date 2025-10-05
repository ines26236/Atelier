def is_mail(str_arg: str) -> (int, int):
    # Vérifier présence de '@'
    if '@' not in str_arg:
        return (0, 2)

    parts = str_arg.split('@')
    corps, domaine = parts

    # Validation du corps
    if not corps or corps[0] == '.' or corps[-1] == '.' or '..' in corps:
        return (0, 1)
    if any(c for c in corps if not (c.isalnum() or c in ['-', '_', '.'])):
        return (0, 1)

    # Validation du domaine
    if not domaine or domaine[0] == '.' or domaine[-1] == '.' or '..' in domaine:
        return (0, 3)
    if any(c for c in domaine if not (c.isalnum() or c in ['-', '.'])):
        return (0, 3)

    # Vérifier présence d'au moins un '.'
    if '.' not in domaine:
        return (0, 4)

    return (1, 0)


def test_mail(mail: str):
    code = is_mail(mail)
    messages = {
        (1, 0): "Adresse valide",
        (0, 1): "Erreur : corps invalide",
        (0, 2): "Erreur : il manque @",
        (0, 3): "Erreur : domaine invalide",
        (0, 4): "Erreur : il manque le ."
    }
    print(mail, "->", messages.get(code, "Erreur inconnue"))


# Tests
test_mail("bisgambiglia_paul@univ-corse.fr")       
test_mail("bisgambiglia_paulOuniv-corse.fr")        
test_mail("bisgambiglia_paul@univ-corsePOINTfr")  
test_mail("@univ-corse.fr")                        
test_mail("jean..dupont@univ-corse.fr")            
test_mail("dupont@.univ-corse.fr")                  
