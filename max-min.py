def process_list():
    # Prompt the user to enter a list of integers
    user_input = input("Enter a list of integers (separated by spaces): ")

    # Convert the input string to a list of integers
    num_list = [int(x) for x in user_input.split()]

    # Print the maxima and minima of the list
    print(f"Maxima: {max(num_list)}")
    print(f"Minima: {min(num_list)}")

    # Print the length of the list
    print(f"Length: {len(num_list)}")

    # Print the sum and average of the elements in the list
    num_sum = sum(num_list)
    print(f"Sum: {num_sum}")
    print(f"Average: {num_sum / len(num_list)}")

    # Calculate and print the product of all the elements in the list
    product = 1
    for num in num_list:
        product *= num
    print(f"Product: {product}")

# Call the function
process_list()
