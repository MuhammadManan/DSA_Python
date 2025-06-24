def sortColors(nums):
    """
    Sorts the input list nums in-place so that all 0s come first, then 1s, then 2s.
    Uses the Dutch National Flag algorithm.
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage:
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    print(nums)  # Output: [0, 0, 1, 1, 2, 2]


    # Additional test case
    nums2 = [1, 2, 0, 1, 2, 0, 1]
    sortColors(nums2)
    print(nums2)  # Output: [0, 0, 1, 1, 1, 2, 2]