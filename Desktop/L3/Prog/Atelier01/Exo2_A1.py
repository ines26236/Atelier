def est_bissextile(annee: int) -> bool:
   
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

annee = int(input("Entrez une année : "))

if est_bissextile(annee):
    print(f"{annee} est une année bissextile ")
else:
    print(f"{annee} n'est pas une année bissextile ")
