def find_min_and_max(arr):
    if not arr:
        raise ValueError("Array is empty")
    minimum = maximum = arr[0]
    for num in arr[1:]:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    return minimum, maximum

# Example usage:
if __name__ == "__main__":
    arr = [3, 1, 7, 0, -2, 8, 5]
    min_val, max_val = find_min_and_max(arr)
    print(f"Minimum: {min_val}, Maximum: {max_val}")