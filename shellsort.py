import time
import random

comparisons = 0
swaps = 0

def shell_sort(arr):
    global comparisons
    global swaps
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
            if j != i:
                arr[j] = temp
                swaps += 1
        gap //= 2

    return arr
def sort_matrix(matrix):
    n = len(matrix)

    # сортировка строк
    for i in range(n):
        matrix[i] = shell_sort(matrix[i])

    # сортировка столбцов
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        col = shell_sort(col)
        for i in range(n):
            matrix[i][j] = col[i]

   
    return matrix

# создание рандонмной матрицы размером 1000 на 1000
n = 100
matrix = [[random.randint(0, 100000) for _ in range(n)] for _ in range(n)]

start_time = time.time()
sorted_matrix = sort_matrix(matrix)
end_time = time.time()

# Вывод первых 10x10 элементов отсортированной матрицы для проверки
for i in range(10):
    print(sorted_matrix[i][:10])

print("Время работы:", end_time - start_time)
print("Число сравнений", comparisons)
print("Количество перестановок", swaps)
