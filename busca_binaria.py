from timeit import default_timer as timer
import random
from math import floor


# Functions defined

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


# Arrays de N aleatório (elementos não-únicos)
n = {"n4": [random.randint(0,10*4) for _ in range(10*4)],
     "n5": [random.randint(0,10*5) for _ in range(10*5)],
     "n6": [random.randint(0,10*6) for _ in range(10*6)],
     "n7": [random.randint(0,10*7) for _ in range(10*7)]
     }

# Sets de N (elementos únicos)
# n4 = list(set(random.sample(range(10*5), 10*4)))
# n5 = list(set(random.sample(range(10*6), 10*5)))
# n6 = list(set(random.sample(range(10*7), 10*6)))
# n7 = list(set(random.sample(range(10*8), 10*7)))

# Q chaves (não únicas)
q = {"q4": [random.randint(0,10*4) for _ in range(10*4)],
     "q5": [random.randint(0,10*5) for _ in range(10*5)],
     "q6": [random.randint(0,10*6) for _ in range(10*6)],
     "q7": [random.randint(0,10*7) for _ in range(10*7)]
     }


# BUSCA SEQUENCIAL
# n = 10^4
print("Busca sequencial:\nn = 10^4\n")

    # q = 10 ^ 4
start = timer()
for i in range(10**4):
    LinearSearch(n['n4'], 10*4, random.randint(0, 10*4))
end = timer()
print(f'q = 10^4, Execução = {end - start:.2f}ms\n')

    # q = 10 ^ 5
start = timer()
for i in range(10**5):
    LinearSearch(n['n4'], 10*5, random.randint(0, 10*4))
end = timer()
print(f'q = 10^5, Execução = {end - start:.2f}ms\n')
    
    # q = 10 ^ 6
start = timer()
for i in range(10**6):
    LinearSearch(n['n4'], 10*6, random.randint(0, 10*4))
end = timer()
print(f'q = 10^6, Execução = {end - start:.2f}ms\n')

    # q = 10 ^ 7
start = timer()
for i in range(10**7):
    LinearSearch(n['n4'], 10*7, random.randint(0, 10*4))
end = timer()
print(f'q = 10^7, Execução = {end - start:.2f}ms\n')

# n = 10^4
# Busca Sequencial

    # q = 10 ^ 4
for i in range(10**4):
    LinearSearch(n['n4'], 10*4, random.randint(0, 10*5))

    # q = 10 ^ 5
for i in range(10**5):
    LinearSearch(n['n5'], 10*5, random.randint(0, 10*6))
    
    # q = 10 ^ 6
for i in range(10**6):
    LinearSearch(n['n6'], 10*6, random.randint(0, 10*7))

    # q = 10 ^ 7
for i in range(10**7):
    LinearSearch(n['n7'], 10*7, random.randint(0, 10*8))


# n = 10^4
# Busca Sequencial

    # q = 10 ^ 4
for i in range(10**4):
    LinearSearch(n['n4'], 10*4, random.randint(0, 10*5))

    # q = 10 ^ 5
for i in range(10**5):
    LinearSearch(n['n5'], 10*5, random.randint(0, 10*6))
    
    # q = 10 ^ 6
for i in range(10**6):
    LinearSearch(n['n6'], 10*6, random.randint(0, 10*7))

    # q = 10 ^ 7
for i in range(10**7):
    LinearSearch(n['n7'], 10*7, random.randint(0, 10*8))