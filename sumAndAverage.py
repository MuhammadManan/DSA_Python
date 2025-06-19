def sum_and_average(arr):
    if not arr:
        return 0, 0
    total = sum(arr)
    avg = total / len(arr)
    return total, avg

if __name__ == "__main__":
    # Example usage
    arr = [10, 20, 30, 40, 50]
    total, avg = sum_and_average(arr)
    print(f"Sum: {total}")
    print(f"Average: {avg}")