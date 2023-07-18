# Ask the user for 7 words
words = []
for i in range(7):
    word = input("Enter a word: ")
    words.append(word)

# Ask the user for a single character
letter = input("Enter a single character: ")

# Loop through the words list
for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The index of the first appearance of '{letter}' in '{word}' is: {index}")
    else:
        print(f"The letter '{letter}' doesn't exist in the word '{word}'.")
