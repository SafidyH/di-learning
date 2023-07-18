def find_longest_word(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    print("The longest word is:", longest_word)

# Example usage
words = ["apple", "banana", "cherry", "durian", "elephant"]
find_longest_word(words)
