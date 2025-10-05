import random
import time
def sort_list(lst):
    lst_copy = lst[:]  
    sorted_list = []

    while lst_copy:
        minimum = lst_copy[0]
        for e in lst_copy:
            if e < minimum:
                minimum = e
        sorted_list.append(minimum)
        lst_copy.remove(minimum)

    return sorted_list

def compare_sort_functions(sort1, sort2, list_sizes, nb_exec):
    results_conf1_1, results_conf1_2 = [], []
    results_conf2_1, results_conf2_2 = [], []
    results_conf3_1, results_conf3_2 = [], []

    for size in list_sizes:
        total1_conf1 = total2_conf1 = 0
        total1_conf2 = total2_conf2 = 0
        total1_conf3 = total2_conf3 = 0

        for i in range(nb_exec):
            # CONF 1 : Liste aléatoire
            base_list = [random.randint(0, size) for _ in range(size)]

            start = time.perf_counter()
            sort1(base_list)
            end = time.perf_counter()
            total1_conf1 += (end - start)

            start = time.perf_counter()
            sort2(base_list)
            end = time.perf_counter()
            total2_conf1 += (end - start)

            # CONF 2 : Liste déjà triée
            sorted_list = list(range(size))

            start = time.perf_counter()
            sort1(sorted_list)
            end = time.perf_counter()
            total1_conf2 += (end - start)

            start = time.perf_counter()
            sort2(sorted_list)
            end = time.perf_counter()
            total2_conf2 += (end - start)

            # CONF 3 : Liste triée à l’envers
            reversed_list = list(range(size, 0, -1))

            start = time.perf_counter()
            sort1(reversed_list)
            end = time.perf_counter()
            total1_conf3 += (end - start)

            start = time.perf_counter()
            sort2(reversed_list)
            end = time.perf_counter()
            total2_conf3 += (end - start)

        results_conf1_1.append(total1_conf1 / nb_exec)
        results_conf1_2.append(total2_conf1 / nb_exec)
        results_conf2_1.append(total1_conf2 / nb_exec)
        results_conf2_2.append(total2_conf2 / nb_exec)
        results_conf3_1.append(total1_conf3 / nb_exec)
        results_conf3_2.append(total2_conf3 / nb_exec)

    return (
        (results_conf1_1, results_conf1_2),
        (results_conf2_1, results_conf2_2),
        (results_conf3_1, results_conf3_2)
    )
