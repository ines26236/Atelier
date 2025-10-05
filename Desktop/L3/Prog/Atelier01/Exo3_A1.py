import math

def distance_3d(xA, yA, zA, xB, yB, zB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2 + (zB - zA)**2)

xA, yA, zA = 1, 2, 3
xB, yB, zB = 4, 6, 8

d = distance_3d(xA, yA, zA, xB, yB, zB)
print("La distance est :", round(d, 2))

