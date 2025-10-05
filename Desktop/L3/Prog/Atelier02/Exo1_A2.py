#Exercice 01:
#01:

def moyenne_dune_lst(ma_liste: list) -> float:
    if len(ma_liste) == 0:  # si la liste est vide
        return 0
    return sum(ma_liste) / len(ma_liste)
print(moyenne_dune_lst([10,15,80,2]))
###### 2 EME FONCTION 
def moyenne(ma_liste: list)->float:
  somme =0
  for i in range(len(ma_liste)):
    
      somme+=ma_liste[i]
      moyenne=somme/len(ma_liste)
  return moyenne 
     
     
L =[1,2,3,5]
print("La moyenne de la liste ",moyenne(L))
