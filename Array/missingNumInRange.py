def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
if __name__ == "__main__":
    nums = [3, 0, 1]
    print(missing_number(nums))  # Output: 2