def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1]