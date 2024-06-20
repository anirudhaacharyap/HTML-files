def count_letter_occurrences(string):
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()

    # Create a dictionary to store the occurrence of each letter
    letter_occurrences = {}

    # Iterate over each character in the string
    for char in string:
        # Check if the character is a letter (ignoring spaces, punctuation, etc.)
        if 'a' <= char <= 'z':
            # If the letter is already in the dictionary, increment its count
            if char in letter_occurrences:
                letter_occurrences[char] += 1
            # If the letter is not in the dictionary, add it with a count of 1
            else:
                letter_occurrences[char] = 1

    # Print the occurrence of each letter
    for letter, count in letter_occurrences.items():
        print(f"Letter '{letter}' occurs {count} times.")

# Example usage:
string = "Hello, World! This is a test string."
count_letter_occurrences(string)
