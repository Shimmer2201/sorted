import time
import random


def generate_file(filename, n):
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(str(random.randint(0, 100000)) + "\n")


def read_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    comparisons = 0
    swaps = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                swaps += 1
                comparisons += 1
            arr[j] = temp
            swaps += 1
        gap //= 2

    return comparisons, swaps


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
comparisons, swaps = shell_sort(union_data)
end_time = time.time()
union_time = end_time - start_time
total_time += union_time
total_comparisons += comparisons
total_swaps += swaps

# Сортировка и замер времени для intersection_data
start_time = time.time()
comparisons, swaps = shell_sort(intersection_data)
end_time = time.time()
intersection_time = end_time - start_time
total_time += intersection_time
total_comparisons += comparisons
total_swaps += swaps

# Сортировка и замер времени для difference_data
start_time = time.time()
comparisons, swaps = shell_sort(difference_data)
end_time = time.time()
difference_time = end_time - start_time
total_time += difference_time
total_comparisons += comparisons
total_swaps += swaps

# Запись результатов в файлы
write_to_file("sorted_union.txt", union_data)
write_to_file("sorted_intersection.txt", intersection_data)
write_to_file("sorted_difference.txt", difference_data)

print("Общее время:", total_time)
print("Общее количество перестановок:", total_swaps)
print("Общее количество сравнений:", total_comparisons)
