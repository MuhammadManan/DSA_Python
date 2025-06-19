def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index

# Example usage:
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = remove_duplicates(nums)
    print(f"After removing duplicates: {nums[:k]}")
    print(f"Number of unique elements: {k}")