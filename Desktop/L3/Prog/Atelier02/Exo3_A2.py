
def separer(lst: list) -> list:
    negatifs = []
    zeros = []
    positifs = []
    
    for x in lst:
        if x < 0:
            negatifs.append(x)
        elif x == 0:
            zeros.append(x)
        else:
            positifs.append(x)
    
    return negatifs  + zeros  +positifs
liste = [0, -5, 3, 0, -2, 7, 0, -1]
print(separer(liste))


def separerV2(lst):
    lsep=[0]*len(lst)
    ipos=len(lst)-1
    ineg=0
    for i in range(len(lst)):
        if lst[i]<0:
            lsep[ineg]=lst[i]
            ineg+=1
        elif lst[i]>0:
            lsep[ipos]=lst[i]
            ipos-=1
    return lsep
liste = [12,4,0,-4,80,0,2,-1]
print(separerV2(liste))



def somme_recursive(l:list)->int:
    if l==[]:
        return 0
    else:
        return l[0]+somme_recursive(l[1:])
L=[1,2,3,4,5]
print("la somme est :", somme_recursive(L))



def factorielle (n: int)->int:
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)
print("le factorielle est:",factorielle(5))
    
    
    