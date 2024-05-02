from timeit import default_timer as timer
import random

# Definição das Funções

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def InsertionSqrtSort(arr):
    n = len(arr)
    sqrt_n = int(n ** 0.5)
    result = []

    for i in range(0, n, sqrt_n):
        partition = arr[i:i+sqrt_n]
        if partition:
            InsertionSort(partition)
            result += partition

    InsertionSort(result)

    return result

def Heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

def HeapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

def HeapSqrtSort(arr):
    n = len(arr)
    sqrt_n = int(n ** 0.5)
    result = []

    for i in range(0, n, sqrt_n):
        partition = arr[i:i+sqrt_n]
        if partition:
            HeapSort(partition)
            result += partition

    HeapSort(result)

    return result


total = 0

# Arrays de N aleatório (elementos não-únicos) - Mais Rápido
# n = {"n4": [random.randint(0,10**4) for _ in range(10**4)],
#      "n5": [random.randint(0,10**5) for _ in range(10**5)],
#      "n6": [random.randint(0,10**6) for _ in range(10**6)],
#      "n7": [random.randint(0,10**7) for _ in range(10**7)],
#      }

print('CRIANDO OS SETS\n')

# Sets de N (elementos únicos)
start = timer()
n4 = list(set(random.sample(range(10**5), 10**4)))
n5 = list(set(random.sample(range(10**6), 10**5)))
n6 =  list(set(random.sample(range(10**7), 10**6)))
n7 = list(set(random.sample(range(10**8), 10**7)))
n8 = list(set(random.sample(range(10**9), 10**8)))
end = timer()
total += end - start
total_set = total
# print(f'Criação dos Sets = {(total_set)*1000:.2f}ms\n')
print('Criação dos Sets = {:.2f}ms\n'.format(total_set * 1000))

# Heap Sort

print('HEAP SORT\n')

print("\nn = 10^4\n")
start = timer()
HeapSqrtSort(n4)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^5\n")
start = timer()
HeapSqrtSort(n5)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^6\n")
start = timer()
HeapSqrtSort(n6)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^7\n")
start = timer()
HeapSqrtSort(n7)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^8\n")
start = timer()
HeapSqrtSort(n8)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

total_heap = total - total_set

# print(f'TEMPO TOTAL HEAP SQRT SORT = {(total_heap)*1000:.2f}ms\n')
print('TEMPO TOTAL HEAP SQRT SORT = {:.2f}ms\n'.format(total_heap * 1000))


# Insertion Sort

print('INSERTION SORT\n')

print("\nn = 10^4\n")
start = timer()
InsertionSqrtSort(n4)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^5\n")
start = timer()
InsertionSqrtSort(n5)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^6\n")
start = timer()
InsertionSqrtSort(n6)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^7\n")
start = timer()
InsertionSqrtSort(n7)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^8\n")
start = timer()
InsertionSqrtSort(n8)
end = timer()
# print(f'Execução = {(end - start)*1000:.2f}ms\n')
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

total_insertion = total - total_heap - total_set

# print(f'TEMPO TOTAL INSERTION SQRT SORT = {(total_insertion)*1000:.2f}ms\n\n')

# print(f'TEMPO TOTAL DE EXECUÇÃO = {(total)*1000:.2f}ms\n')

print('TEMPO TOTAL INSERTION SQRT SORT = {:.2f}ms\n\n'.format(total_insertion * 1000))
print('TEMPO TOTAL DE EXECUÇÃO = {:.2f}ms\n'.format(total * 1000))
