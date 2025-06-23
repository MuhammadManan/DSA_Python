def reverse_string(s):
    """
    Reverses a list of characters in-place.

    Args:
        s (list): List of characters to reverse.

    Returns:
        None: The list is modified in-place.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Example usage:
arr = ['h', 'e', 'l', 'l', 'o']
reverse_string(arr)
print(arr)  # Output: ['o', 'l', 'l', 'e', 'h']