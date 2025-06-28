def max_sum_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0

    for i, num in enumerate(arr):
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
        if current_sum < 0:
            current_sum = 0
            s = i + 1
    return max_sum, arr[start:end+1]

# Example usage:
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = max_sum_subarray(arr)
    print("Maximum sum:", max_sum)
    print("Subarray:", subarray)