def count_occurrences(lst, element):
    """
    Counts the number of times `element` appears in `lst`.

    Args:
        lst (list): The list to search.
        element: The element to count.

    Returns:
        int: Number of occurrences of `element` in `lst`.
    """
    return lst.count(element)

# Example usage:
if __name__ == "__main__":
    data = [1, 2, 3, 2, 4, 2, 5]
    target = 2
    print(f"{target} occurs {count_occurrences(data, target)} times in the list.")