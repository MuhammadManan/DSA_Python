def merge_two_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements
    while i < n:
        merged.append(arr1[i])
        i += 1
    while j < m:
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage:
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
# print(merge_two_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]