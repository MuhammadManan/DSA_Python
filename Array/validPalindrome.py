import re

def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage:
if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(is_palindrome(test_str))  # Output: True