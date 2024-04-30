from timeit import default_timer as timer
import random
import math

# Definição das Classes
class Heap:
    def __init__(self, data):
        self.data = data
        self.next = None

# Definição das Funções
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def InsertionSqrtSort(arr):
    part_size = int(math.sqrt(len(arr)))

    sorted_arr = []

    for i in range(0, len(arr), part_size):
        part = arr[i:i+part_size]
        InsertionSort(part)
        sorted_arr.append(part[-1])

    return sorted_arr


def HeapSort(arr):
    pass


def HeapSqrtSort(arr):
    pass

def IsSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True



total = 0

# Arrays de N aleatório (elementos não-únicos) - Mais Rápido
# n = {"n4": [random.randint(0,10**4) for _ in range(10**4)],
#      "n5": [random.randint(0,10**5) for _ in range(10**5)],
#      "n6": [random.randint(0,10**6) for _ in range(10**6)],
#      "n7": [random.randint(0,10**7) for _ in range(10**7)],
#      }

print(f'CRIANDO OS SETS\n')

start = timer()
# Sets de N (elementos únicos)
n4 = list(set(random.sample(range(10**9), 10**4)))
n5 = list(set(random.sample(range(10**9), 10**5)))
n6 =  list(set(random.sample(range(10**9), 10**6)))
n7 = list(set(random.sample(range(10**9), 10**7)))
n8 = list(set(random.sample(range(10**9), 10**8)))
end = timer()
print(f'Criação dos Sets = {(end - start)*1000:.2f}ms\n')

# Insertion Sort

total_insertion = 0
print("\nn = 10^4\n")
start = timer()
InsertionSqrtSort(n4)
end = timer()
print(f'Execução = {(end - start)*1000:.2f}ms\n')
total += end - start

print("\nn = 10^5\n")
start = timer()
InsertionSqrtSort(n5)
end = timer()
print(f'Execução = {(end - start)*1000:.2f}ms\n')
total += end - start

print("\nn = 10^6\n")
start = timer()
InsertionSqrtSort(n6)
end = timer()
print(f'Execução = {(end - start)*1000:.2f}ms\n')
total += end - start

print("\nn = 10^7\n")
start = timer()
InsertionSqrtSort(n7)
end = timer()
print(f'Execução = {(end - start)*1000:.2f}ms\n')
total += end - start

print("\nn = 10^8\n")
start = timer()
InsertionSqrtSort(n8)
end = timer()
print(f'Execução = {(end - start)*1000:.2f}ms\n')
total += end - start
