import string
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else f"The word '{word}' is not found in the text."

    def most_common_word(self):
        words = self.text.lower().split()
        word_counts = Counter(words)
        return word_counts.most_common(1)[0][0]

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as file:
            text = file.read()
        return cls(text)


class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self):
        stop_words = ["a", "an", "the", "and", "in", "on", "of", "to", "for", "with"]
        words = self.text.lower().split()
        return " ".join(word for word in words if word not in stop_words)

    def remove_special_characters(self):
        return "".join(char for char in self.text if char.isalnum() or char.isspace())

# Part I - Analyzing a simple string
text = "A good book would sometimes cost as much as a good house."
text_analyzer = Text(text)
print("Frequency of 'good':", text_analyzer.word_frequency("good"))
print("Most common word:", text_analyzer.most_common_word())
print("Unique words:", text_analyzer.unique_words())

# Part II - Analyzing from external text file
external_text_analyzer = Text.from_file("the_stranger.txt")
print("\nFrequency of 'stranger':", external_text_analyzer.word_frequency("stranger"))
print("Most common word:", external_text_analyzer.most_common_word())
print("Unique words:", external_text_analyzer.unique_words())

# Bonus - Text Modification
text_modifier = TextModification(text)
print("\nText without punctuation:")
print(text_modifier.remove_punctuation())
print("\nText without stop words:")
print(text_modifier.remove_stop_words())
print("\nText without special characters:")
print(text_modifier.remove_special_characters())
