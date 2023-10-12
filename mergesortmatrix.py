import time
import random

comparisons = 0
swaps = 0


def merge_sort(arr):
    global comparisons
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    global comparisons
    global swaps
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        comparisons += 1
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
            swaps += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result


def sort_matrix(matrix):
    n = len(matrix)

    # Сортировка строк
    for i in range(n):
        matrix[i] = merge_sort(matrix[i])

    # Сортировка столбцов
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        col = merge_sort(col)
        for i in range(n):
            matrix[i][j] = col[i]

    return matrix


# Создание случайной матрицы размером 1000x1000
n = 100
matrix = [[random.randint(0, 100000) for _ in range(n)] for _ in range(n)]

start_time = time.time()
sorted_matrix = sort_matrix(matrix)
end_time = time.time()

# Вывод первых 10x10 элементов отсортированной матрицы для проверки
for i in range(10):
    print(sorted_matrix[i][:10])

print("Время работы:", end_time - start_time)
print("Число сравнений:", comparisons)
print("Число перестановок:", swaps)
