def reverse_sentence(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Reverse the order of the words
    reversed_words = list(reversed(words))

    # Join the reversed words to form the reversed sentence
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence

# Example usage
sentence = "You have entered a wrong domain"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
