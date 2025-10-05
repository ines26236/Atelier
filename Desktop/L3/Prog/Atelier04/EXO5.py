import time
import random
import matplotlib.pyplot as plt
import numpy as np

def perf_mix(func1, func2, list_sizes, nb_exec):
    results_func1 = []
    results_func2 = []

    for size in list_sizes:
        # On crée une liste triée de la taille demandée
        base_list = list(range(size))

        # Mesure du temps pour func1
        total_time1 = 0
        for _ in range(nb_exec):
            # On passe une copie de la liste pour ne pas modifier l'originale
            start = time.perf_counter()
            func1(base_list[:])  # [:] crée une copie
            end = time.perf_counter()
            total_time1 += (end - start)
        moyenne1 = total_time1 / nb_exec
        results_func1.append(moyenne1)

        # Mesure du temps pour func2
        total_time2 = 0
        for _ in range(nb_exec):
            list_copy = base_list[:]  #  une copie pour ne pas réutiliser une liste modifiée
            start = time.perf_counter()
            func2(list_copy)  # random.shuffle modifie la liste en place
            end = time.perf_counter()
            total_time2 += (end - start)
        moyenne2 = total_time2 / nb_exec
        results_func2.append(moyenne2)

    return (results_func1, results_func2)
# Ta fonction mix_list qu'on a définie sans utiliser shuffle
def mix_list(lst):
   
    temp = lst[:]
    mixed = []
    while temp:
        i = random.randint(0, len(temp) - 1)
        mixed.append(temp.pop(i))
    return mixed


# Appel de la fonction de comparaison
list_sizes = [10, 100, 500, 1000, 5000, 10000]
nb_exec = 10

results = perf_mix(mix_list, random.shuffle, list_sizes, nb_exec)

print("Temps moyens pour mix_list :", results[0])
print("Temps moyens pour shuffle  :", results[1])

# Affichage des courbes
x_axis = list_sizes
y1, y2 = results

plt.plot(x_axis, y1, 'bo-', label='mix_list (sans shuffle)')
plt.plot(x_axis, y2, 'r*-', label='random.shuffle')

plt.xlabel('Taille de la liste')
plt.ylabel('Temps moyen (secondes)')
plt.title('Comparaison des temps de mélange')
plt.legend()
plt.grid(True)
plt.show()
