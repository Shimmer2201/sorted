import time
import random


def generate_file(filename, n):
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(str(random.randint(0, 100000)) + "\n")


def read_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, left_comparisons, left_swaps = merge_sort(left)
    right, right_comparisons, right_swaps = merge_sort(right)

    merged_arr, merge_comparisons, merge_swaps = merge(left, right)

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    total_swaps = left_swaps + right_swaps + merge_swaps

    return merged_arr, total_comparisons, total_swaps


def merge(left, right):
    result = []
    i = j = 0
    comparisons = swaps = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        swaps += 1

    result.extend(left[i:])
    swaps += len(left[i:])
    result.extend(right[j:])
    swaps += len(right[j:])

    return result, comparisons, swaps


def write_to_file(filename, arr):
    with open(filename, 'w') as f:
        for item in arr:
            f.write(str(item) + "\n")


# Создание двух файлов со случайными числами
generate_file("file1.txt", 2500)
generate_file("file2.txt", 2500)

data1 = read_file("file1.txt")
data2 = read_file("file2.txt")

# Выполнение операций
union_data = list(set(data1).union(set(data2)))
intersection_data = list(set(data1).intersection(set(data2)))
difference_data = list(set(data1).difference(set(data2)))

# Замеры времени, сравнений и перестановок
total_time = 0
total_comparisons = 0
total_swaps = 0

# Сортировка и замер времени для union_data
start_time = time.time()
sorted_union, union_comparisons, union_swaps = merge_sort(union_data)
end_time = time.time()
union_time = end_time - start_time
total_time += union_time
total_comparisons += union_comparisons
total_swaps += union_swaps

# Сортировка и замер времени для intersection_data
start_time = time.time()
sorted_intersection, intersection_comparisons, intersection_swaps = merge_sort(intersection_data)
end_time = time.time()
intersection_time = end_time - start_time
total_time += intersection_time
total_comparisons += intersection_comparisons
total_swaps += intersection_swaps

# Сортировка и замер времени для difference_data
start_time = time.time()
sorted_difference, difference_comparisons, difference_swaps = merge_sort(difference_data)
end_time = time.time()
difference_time = end_time - start_time
total_time += difference_time
total_comparisons += difference_comparisons
total_swaps += difference_swaps

# Запись результатов в файлы
write_to_file("sorted_union.txt", sorted_union)
write_to_file("sorted_intersection.txt", sorted_intersection)
write_to_file("sorted_difference.txt", sorted_difference)

print("Общее время:", total_time)
print("Общее количество перестановок:", total_comparisons)
print("Общее количество сравнений:", total_swaps)
