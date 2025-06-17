def reverse_array(arr):
    return arr[::-1]

# Example usage
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    reversed_array = reverse_array(array)
    print("Original array:", array)
    print("Reversed array:", reversed_array)


    def reverse_array_manual(arr):
        reversed_arr = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_arr.append(arr[i])
        return reversed_arr

    # Example usage
    if __name__ == "__main__":
        manual_reversed_array = reverse_array_manual(array)
        print("Manually reversed array:", manual_reversed_array)