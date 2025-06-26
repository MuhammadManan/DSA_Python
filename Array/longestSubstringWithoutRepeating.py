def length_of_longest_substring(s: str) -> int:
    # Set to store unique characters in the current window
    char_set = set()
    # Left pointer of the sliding window
    left = 0
    # Variable to keep track of the maximum length found
    max_len = 0

    # Iterate through the string with the right pointer
    for right in range(len(s)):
        # If the character is already in the set, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Update the maximum length if needed
        max_len = max(max_len, right - left + 1)
    return max_len

# Example usage:
if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))  # Output: 3