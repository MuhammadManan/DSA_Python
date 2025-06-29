import heapq

def merge_two_sorted_arrays(arr1, arr2):
    return list(heapq.merge(arr1, arr2))

# Example usage:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_two_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]
