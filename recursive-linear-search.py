def recursive_linear_search(arr, target, index=0):
    """
    Performs recursive linear search on an array.

    Args:
        arr (list): A list of elements.
        target: The element to search for.
        index (int): The current index to search (default=0).

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    if index >= len(arr):
        return -1  # not found
    if arr[index] == target:
        return index
    return recursive_linear_search(arr, target, index + 1)

# Example usage:
arr = [4, 2, 7, 1, 3, 9, 6, 5, 8]
target = 5
result = recursive_linear_search(arr, target)

if result!= -1:
    print("Element " + str(target) + " found at index " + str(result))
else:
    print("Element " + str(target) + " not found in the array")
