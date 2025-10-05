#Partie 1 – Récursivité  
    #Q1:
def somme_recursive(lst:list)->int:
    résultat=0
    if len(lst) == 0:  
        return 0
    résultat= lst[0]+somme_recursive(lst[1:]) 
    return résultat
ma_liste = [1, 2, 3, 4, 5]

print("La somme de la liste est :",somme_recursive(ma_liste))  
 

     #Q2
def factorielle(x:int)->int:
     if x==0 or x==1:
      return 1
     return x* factorielle(x-1)
x = 5
print(f"Le factorielle de {x} est: {factorielle(x)}")
    #Q3

def longeur_récursive(lst:list)->int:
    if len(lst)==0:
        return 0
    return 1+longeur_récursive(lst[1:])
L=[10,20,30,35]
print ("Le nombre d'élémments dans ma liste est:",longeur_récursive(L))

    #Q4
def recursive_minimum (lst:list)->int:
    if len (lst)==1:
        return lst[0]
    else:
      min_rest=recursive_minimum(lst[1:])
      if lst[0]<min_rest:
        return lst[0]
      else:
          return min_rest
L=[40,5,32,10,15,2]
print("le minimum est :", recursive_minimum(L))
    #Q5
def récursive_listPaires(lst:list)->list:
    if len(lst)==0:
        return []
    else:
        rest_paires=récursive_listPaires(lst[1:])
        if lst[0]%2==0:
            return [lst[0]]+rest_paires
        else:
            return rest_paires
L=[12,30,2,45,11,6,5]
print ("la liste des nombres paires est :",récursive_listPaires(L))
    #Q6
def concapt_list(LL:list)->list:
    if len(LL)==0:
        return []
    else:
        return [LL[0]]+concapt_list(LL[1:])
L=[[0,1],[2,3],[4],[6,7]]
print("La liste concarénée est:",concapt_list(L)) #cette fonction n'affiche pas le mm résultat

    #Q7
def incluse(lst1:list,lst2:list)->bool:
    if len(lst1)==0:
        return True
    elif len (lst2)==0:
        return False
    elif lst1[0]in lst2:
        return incluse(lst1[1:],lst2)
    else:
        return False
L1=[1,2,3,7,8]
L2=[]
print("L1 est elle incluse dans L2 ?:",incluse(L1,L2))














    