def second_largest(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None

# Example usage
arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr))  # Output: 34