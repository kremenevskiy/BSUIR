import random
import sys


def partition(arr, start, end):
    pivot_i = random.randint(start, end)
    pivot = arr[pivot_i]

    arr[start], arr[pivot_i] = arr[pivot_i], arr[start]

    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1

        while low <= high and arr[low] <= pivot:
            low += 1

        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break

    arr[start], arr[high] = arr[high], arr[start]
    return high


def quick_sort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)
    quick_sort(arr, start, p-1)
    quick_sort(arr, p+1, end)


arr = []
for i in range(1000000):
    arr.append(random.randint(0, 100))


sys.setrecursionlimit(max(sys.getrecursionlimit(), len(arr)+100))

quick_sort(arr, 0, len(arr) - 1)
for i in arr:
    print(i, end=' ')