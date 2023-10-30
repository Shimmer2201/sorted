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
    global comparisons, swaps
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

    # Добавляем оставшиеся элементы
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result

# Здесь для примера создадим два случайных массива размером 2500
n = 2500
arr1 = [random.randint(0, 100000) for _ in range(n)]
arr2 = [random.randint(0, 100000) for _ in range(n)]

sorted_arr1 = merge_sort(arr1)
sorted_arr2 = merge_sort(arr2)

# Создание третьего массива и его сортировка
arr3 = sorted_arr1 + sorted_arr2
start_time = time.time()
sorted_arr3 = merge_sort(arr3)
end_time = time.time()

print("Слиянием")
print("Время сортировки третьего массива:", end_time - start_time)
print("Число сравнений:", comparisons)
print("Число перестановок:", swaps)
