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


# Создание случайного массива размером 2500
n = 2500
arr = [random.randint(0, 100000) for _ in range(n)]

start_time = time.time()
shell_sort(arr)
end_time = time.time()

print("Первые 10 элементов отсортированного массива:", arr[:10])
print("Время работы:", end_time - start_time)
print("Число сравнений:", comparisons)
print("Число перестановок:", swaps)
