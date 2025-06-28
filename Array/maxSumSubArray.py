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

