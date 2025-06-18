def contains_value(arr, value):
    """
    Check if the array contains the specified value.

    Args:
        arr (list): The list to search.
        value: The value to find.

    Returns:
        bool: True if value is found, False otherwise.
    """
    for item in arr:
        if item == value:
            return True
    return False

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    value = 3
    print(contains_value(arr, value))  # Output: True