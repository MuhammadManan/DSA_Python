def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example usage:
if __name__ == "__main__":
    arr = ["flower", "flow", "flight"]
    print(longest_common_prefix(arr))  # Output: "fl"