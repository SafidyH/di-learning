word = input("Enter a word: ")  # Ask the user for a word

indexes_dict = {}  # Initialize an empty dictionary

# Iterate over each letter in the word
for index, letter in enumerate(word):
    # Check if the letter is already a key in the dictionary
    if letter in indexes_dict:
        indexes_dict[letter].append(index)  # Add the index to the existing list of indexes
    else:
        indexes_dict[letter] = [index]  # Create a new list with the index as the value

print(indexes_dict)  # Print the resulting dictionary
