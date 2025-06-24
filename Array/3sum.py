from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates for i
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates for left and right
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return res

# Example usage:
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]


    # Additional test cases
    test_cases = [
        ([], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]

    for nums, expected in test_cases:
        result = threeSum(nums)
        print(f"Input: {nums} => Output: {result} | Expected: {expected}")