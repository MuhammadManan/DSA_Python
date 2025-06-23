def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into a single sorted array.

    Args:
        arr1 (list): First sorted array.
        arr2 (list): Second sorted array.

    Returns:
        list: Merged sorted array.
    """
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
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    print(merge_sorted_arrays(arr1, arr2))