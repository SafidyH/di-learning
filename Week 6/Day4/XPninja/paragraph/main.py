paragraph = """
The quick brown fox jumps over the lazy dog. This sentence is an example. Another example sentence follows. The fox and the dog are friends. They play together in the park. The dog enjoys chasing the fox. The fox runs fast to escape the dog. It's a beautiful day outside.
"""

# How many characters the paragraph contains
char_count = len(paragraph)
print("Character count:", char_count)

# How many sentences the paragraph contains
sentence_count = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
print("Sentence count:", sentence_count)

# How many words the paragraph contains
word_list = paragraph.split()
word_count = len(word_list)
print("Word count:", word_count)

# How many unique words the paragraph contains
unique_words = set(word_list)
unique_word_count = len(unique_words)
print("Unique word count:", unique_word_count)

# Bonus: How many non-whitespace characters the paragraph contains
non_whitespace_count = len(paragraph.replace(" ", ""))
print("Non-whitespace character count:", non_whitespace_count)

# Bonus: The average amount of words per sentence in the paragraph
average_words_per_sentence = word_count / sentence_count
print("Average words per sentence:", average_words_per_sentence)

# Bonus: The amount of non-unique words in the paragraph
non_unique_words_count = word_count - unique_word_count
print("Non-unique word count:", non_unique_words_count)
