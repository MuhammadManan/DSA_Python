def longest_common_prefix(strs):
    # Return empty string if input list is empty
    if not strs:
        return ""
    # Initialize prefix as the first string
    prefix = strs[0]
    # Iterate over the rest of the strings
    for s in strs[1:]:
        # Reduce prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # Remove last character from prefix
            if not prefix:
                return ""  # No common prefix found
    return prefix  # Return the longest common prefix found

# Example usage:
if __name__ == "__main__":
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
         
    ]
    for arr, expected in test_cases:
        result = longest_common_prefix(arr)
        print(f"Input: {arr}\nOutput: '{result}' (Expected: '{expected}')\n")