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
arr1 = [random.randint(0, 100000) for _ in range(n)]
arr2 = [random.randint(0, 100000) for _ in range(n)]

sorted_arr1 = shell_sort(arr1)
sorted_arr2 = shell_sort(arr2)

arr3 = sorted_arr1 + sorted_arr2
start_time = time.time()
sorted_arr3 = shell_sort(arr3)
end_time = time.time()

print("Шелла")
print("Время работы:", end_time - start_time)
print("Число сравнений:", comparisons)
print("Число перестановок:", swaps)
