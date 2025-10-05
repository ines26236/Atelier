def est_triangle(a: float, b: float, c: float) -> bool:
    
    return (a + b > c) and (a + c > b) and (b + c > a)

a = float(input("Longueur a : "))
b = float(input("Longueur b: "))
c = float(input("Longueur c: "))

if est_triangle(a, b, c):
    print("Ces segments peuvent former un triangle ")
else:
    print("Ces segments ne peuvent pas former un triangle ")
