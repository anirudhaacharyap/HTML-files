def binary_search(list, elem_to_search):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if elem_to_search == list[mid]:
            return mid
        elif elem_to_search < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list1 = ["Pratyaksh","Udit","Vibhas"]
elem_to_search = "Vibhas"

result = binary_search(list1, elem_to_search)

if result == -1:
    print("Element not found!")
else:
    print("Element found at index ", result)
