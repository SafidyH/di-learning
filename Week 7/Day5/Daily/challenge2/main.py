def longest_word(sentence):
    word_list = sentence.split()  # Split the sentence into a list of words
    longest = max(word_list, key=len)  # Find the longest word based on length
    return longest

# Test the function
sentence = input("Enter a sentence: ")
longest = longest_word(sentence)
print(longest)
