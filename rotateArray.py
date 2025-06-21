def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k > n
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(arr, k)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]