def most_frequent_words(paragraph):
    # Convert the paragraph to lowercase and split it into individual words
    words = paragraph.lower().replace('.', '').replace(',', '').replace(';', '').replace(':', '').split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Sort the words by frequency in descending order
    sorted_word_freq = sorted(word_freq.items(), key=get_frequency, reverse=True)

    # Print the 10 most frequent words
    print("Top 10 most frequent words:")
    for word, freq in sorted_word_freq[:10]:
        print(f"{word}: {freq}")

def get_frequency(item):
    return item[1]

# Example usage:
paragraph = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
most_frequent_words(paragraph)
