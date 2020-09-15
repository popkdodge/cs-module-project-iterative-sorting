def linear_search(arr, target):
    # Your code here
    for count, item in enumerate(arr):
        if item == target:
            return count
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint
        
        elif arr[midpoint] > target:
            right = midpoint - 1
        
        else:
            left = midpoint + 1

    return -1  # not found
