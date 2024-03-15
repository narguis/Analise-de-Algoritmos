from timeit import default_timer as timer
import random
from math import floor


# Definição das Funções

def LinearSearch(array: list[int], size: int, key:int) -> int:
    for i in range(size):
        if array[i] == key:
            return i
    
    return -1

def OptimizedLinearSearch(sorted_array: list[int], size: int, key:int) -> int:
    for i in range(size):
        if sorted_array[i] == key:
            return i
        elif sorted_array[i] > key:
            break
    
    return -1

def BinarySearch(sorted_array: list[int], size: int, key: int) -> int:
    if size == 0:
        return -1

    mid = floor(size / 2)
    if sorted_array[mid] == key:
        return mid
    elif key < sorted_array[mid]:
        return BinarySearch(sorted_array[:mid], mid, key)
    else:
        result = BinarySearch(sorted_array[mid + 1:], size - mid - 1, key)
        if result != -1:
            return mid + 1 + result
        else:
            return -1


# Arrays de N aleatório (elementos não-únicos) - Mais Rápido
# n = {"n4": [random.randint(0,10**4) for _ in range(10**4)],
#      "n5": [random.randint(0,10**5) for _ in range(10**5)],
#      "n6": [random.randint(0,10**6) for _ in range(10**6)],
#      "n7": [random.randint(0,10**7) for _ in range(10**7)],
#      }

# Sets de N (elementos únicos)
n4 = list(set(random.sample(range(10**5), 10**4)))
n5 = list(set(random.sample(range(10**6), 10**5)))
n6 =  list(set(random.sample(range(10**7), 10**6)))
n7 = list(set(random.sample(range(10**8), 10**7)))

# Arrays de chaves Q (chaves não-únicas) - Mais Rápido
# q = {"q2": [random.randint(0,10**7) for _ in range(10**2)],
#      "q3": [random.randint(0,10**7) for _ in range(10**3)],
#      "q4": [random.randint(0,10**7) for _ in range(10**4)],
#      "q5": [random.randint(0,10**7) for _ in range(10**5)]
#      }

# Sets de chaves Q (chaves únicas)
q2 = list(set(random.sample(range(10**7), 10**2)))
q3 = list(set(random.sample(range(10**7), 10**3)))
q4 = list(set(random.sample(range(10**7), 10**4)))
q5 = list(set(random.sample(range(10**7), 10**5)))


# BUSCA SEQUENCIAL
# n = 10^4
total = 0
print("BUSCA SEQUENCIAL:\n\nn = 10^4\n")

    # q = 10 ^ 2
start = timer()
for i in range(len(q2)):
    LinearSearch(n4, len(n4), q2[i])
end = timer()
print(f'q = 10^2, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 3
start = timer()
for i in range(len(q3)):
    LinearSearch(n4, len(n4), q3[i])
end = timer()
print(f'q = 10^3, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 4
start = timer()
for i in range(len(q4)):
    LinearSearch(n4, len(n4), q4[i])
end = timer()
print(f'q = 10^4, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 5
start = timer()
for i in range(len(q5)):
    LinearSearch(n4, len(n4), q5[i])
end = timer()
print(f'q = 10^5, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

print(f'Total (n = 10^4) =  {total*1000:.2f}ms ou {total:.2f}s')
print('.\n')

# n = 10^5
total = 0
print("\nn = 10^5\n")

    # q = 10 ^ 2
start = timer()
for i in range(len(q2)):
    LinearSearch(n5, len(n5), q2[i])
end = timer()
print(f'q = 10^2, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 3
start = timer()
for i in range(len(q3)):
    LinearSearch(n5, len(n5), q3[i])
end = timer()
print(f'q = 10^3, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 4
start = timer()
for i in range(len(q4)):
    LinearSearch(n5, len(n5), q4[i])
end = timer()
print(f'q = 10^4, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 5
start = timer()
for i in range(len(q5)):
    LinearSearch(n5, len(n5), q5[i])
end = timer()
print(f'q = 10^5, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

print(f'Total (n = 10^5) =  {total*1000:.2f}ms ou {total:.2f}s')
print('.\n')

# n = 10^6
total = 0
print("\nn = 10^6\n")

    # q = 10 ^ 2
start = timer()
for i in range(len(q2)):
    LinearSearch(n6, len(n6), q2[i])
end = timer()
print(f'q = 10^2, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 3
start = timer()
for i in range(len(q3)):
    LinearSearch(n6, len(n6), q3[i])
end = timer()
print(f'q = 10^3, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 4
start = timer()
for i in range(len(q4)):
    LinearSearch(n6, len(n6), q4[i])
end = timer()
print(f'q = 10^4, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 5
start = timer()
for i in range(len(q5)):
    LinearSearch(n6, len(n6), q5[i])
end = timer()
print(f'q = 10^5, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

print(f'Total (n = 10^6) =  {total*1000:.2f}ms ou {total:.2f}s')
print('.\n')

# n = 10^7
total = 0
print("\nn = 10^7\n")

    # q = 10 ^ 2
start = timer()
for i in range(len(q2)):
    LinearSearch(n7, len(n7), q2[i])
end = timer()
print(f'q = 10^2, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 3
start = timer()
for i in range(len(q3)):
    LinearSearch(n7, len(n7), q3[i])
end = timer()
print(f'q = 10^3, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 4
start = timer()
for i in range(len(q4)):
    LinearSearch(n7, len(n7), q4[i])
end = timer()
print(f'q = 10^4, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

    # q = 10 ^ 5
start = timer()
for i in range(len(q5)):
    LinearSearch(n7, len(n7), q5[i])
end = timer()
print(f'q = 10^5, Execução = {(end - start)*1000:.2f}ms\n')
total += end-start

print(f'Total (n = 10^7) =  {total*1000:.2f}ms ou {total:.2f}s')
print('.\n')