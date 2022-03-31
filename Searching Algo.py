# Searching Algorithms

# Binary Search
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


# Complexity of Binary Search is O(log n)
# Best case: O(1)
# Worst case: O(log n)
# Logic of Binary Search:
# 1. Find the middle element of the array
# 2. If the middle element is the element we are looking for, return the index
# 3. If the middle element is greater than the element we are looking for, then the element we are looking for must be in the left half of the array
# 4. If the middle element is less than the element we are looking for, then the element we are looking for must be in the right half of the array
# 5. Repeat steps 2-4 until the middle element is the element we are looking for or the left and right halves are empty
# 6. If the element is not found, return -1


# Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Complexity of Linear Search is O(n)
# Best case: O(1)
# Worst case: O(n)
# Logic of Linear Search
# 1. If the element is present at the first index then return 0
# 2. If the element is present at the last index then return n-1
# 3. If the element is present at the middle index then return mid
# 4. If the element is not present in the array then return -1
