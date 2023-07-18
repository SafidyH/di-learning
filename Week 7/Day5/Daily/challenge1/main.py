def sort_words(words):
    word_list = words.split(',')  # Split the input string into a list of words
    sorted_words = sorted(word_list)  # Sort the words alphabetically
    sorted_sequence = ','.join(sorted_words)  # Join the sorted words with commas
    return sorted_sequence

# Test the function
input_words = input("Enter a comma-separated sequence of words: ")
sorted_sequence = sort_words(input_words)
print(sorted_sequence)
