import random

def build_dict(lst: list) -> dict:
    
    dictionnaire_mots = {}
    for mot in lst:
        taille = len(mot)
        if taille not in dictionnaire_mots:
            dictionnaire_mots[taille] = []
        dictionnaire_mots[taille].append(mot)
    return dictionnaire_mots
#2:

def select_word(sorted_words: dict, word_len: int) -> str:
   
    if word_len not in sorted_words:
        print("aucun mot")
    return random.choice(sorted_words[word_len])


lst = ["paris", "madrid", "berlin", "londres", "newyork"]
dictionnaire_mots = build_dict(lst)
print(dictionnaire_mots)  


mot_aleatoire = select_word(dictionnaire_mots, 5)
print("Mot choisi:", mot_aleatoire)
