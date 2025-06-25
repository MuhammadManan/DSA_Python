def trap(height):
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    trapped_water = 0


# Example usage:
if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(arr))  # Output: 6