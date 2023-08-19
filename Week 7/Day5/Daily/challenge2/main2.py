def longest_word(sentence):
    words = sentence.split()
    longest_word = ""

    for word in words:
        # Removing non-alphanumeric characters from the word to calculate its length correctly
        clean_word = ''.join(c for c in word if c.isalnum())

        if len(clean_word) > len(longest_word):
            longest_word = clean_word

    return longest_word

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = longest_word(sentence)
    print("Longest word:", result)
