import random

def gen_list_random_int(int_nbr=10, int_binf=0, int_bsup=10):
    
    return [random.randint(int_binf, int_bsup -1) for _ in range(int_nbr)]


print(gen_list_random_int())           
print(gen_list_random_int(5))         
print(gen_list_random_int(5, 20, 30))  