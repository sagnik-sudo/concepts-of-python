# Selection Sort Python
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Complexity of Selection Sort is O(n^2)
# Best case: O(n^2)
# Worst case: O(n^2)
# Logic of Selection Sort:
# 1. Find the minimum element in the array
# 2. Swap the minimum element with the first element
# 3. Repeat steps 1-2 for the remaining elements


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Complexity of Bubble Sort is O(n^2)
# Best case: O(n)
# Worst case: O(n^2)
# Logic of Bubble Sort:
# 1. Compare the first element with the second element
# 2. If the first element is greater than the second element, swap them
# 3. Repeat steps 1-2 for the remaining elements
# 4. Repeat steps 1-3 for the entire array


# Insertion Sort Python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Complexity of Insertion Sort is O(n^2)
# Best case: O(n)
# Worst case: O(n^2)
# Logic of Insertion Sort:
# 1. Find the minimum element in the array
# 2. Swap the minimum element with the first element
# 3. Repeat steps 1-2 for the remaining elements


# Merge Sort Python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


# Complexity of Merge Sort is O(n log n)
# Best case: O(n log n)
# Worst case: O(n log n)
# Logic of Merge Sort:
# 1. Divide the array into two halves
# 2. Sort the two halves
# 3. Merge the two sorted halves
# 4. Repeat steps 1-3 until the array is sorted


# Quick Sort Python
def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        right = [i for i in arr[1:] if i > pivot]
        quick_sort(left)
        quick_sort(right)
        arr[:] = left + [pivot] + right
    return arr


# Complexity of Quick Sort is O(n log n)
# Best case: O(n log n)
# Worst case: O(n^2)
# Logic of Quick Sort:
# 1. Pick a pivot element
# 2. Partition the array around the pivot element
# 3. Repeat steps 1-2 for the left and right halves
# 4. Repeat steps 1-3 for the entire array

# Tim Sort Python
def tim_sort(arr):
    gap = 1
    while gap < len(arr):
        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i += 1
        gap *= 2
    return arr

# Complexity of Tim Sort is O(n log n)
# Best case: O(n log n)
# Worst case: O(n^2)
# Logic of Tim Sort:
# 1. Pick a gap size
# 2. Compare the elements at the current gap size
# 3. If the element at the current gap size is greater than the next element, swap them
# 4. Repeat steps 2-3 for the remaining elements
# 5. Repeat steps 1-4 until the array is sorted
