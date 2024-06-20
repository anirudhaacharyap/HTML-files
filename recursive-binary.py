def recursive_binary_search(arr, target, low, high):
    """
    Performs recursive binary search on a sorted array.

    Args:
        arr (list): A sorted list of elements.
        target: The element to search for.
        low (int): The lower bound of the current search range.
        high (int): The upper bound of the current search range.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    if low > high:
        return -1  # not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return recursive_binary_search(arr, target, low, mid - 1)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = recursive_binary_search(arr, target, 0, len(arr) - 1)

if result!= -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
