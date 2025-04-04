# Проанализируйте время выполнения сортировки слиянием на
# списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка пузырьком

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def generate_random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

def test_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr.copy())
    end_time = time.time()
    return end_time - start_time

sizes = [10, 100, 1000]
for size in sizes:
    arr = generate_random_list(size)

    merge_time = test_sorting_algorithm(merge_sort, arr)
    bubble_time = test_sorting_algorithm(bubble_sort, arr)

    print(f"\nРазмер списка: {size} элементов")
    print(f"MergeSort: {merge_time:.6f} сек")
    print(f"BubbleSort: {bubble_time:.6f} сек")