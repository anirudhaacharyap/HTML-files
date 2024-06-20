def linear_search(arr, target):
    """
    Performs linear search on an array.

    Args:
        arr (list): A list of elements.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # not found

# Example usage:
arr = [4, 2, 7, 1, 3, 9, 6, 5, 8]
target = 5
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
