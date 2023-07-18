from collections import Counter

input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

words = input_text.split()

word_frequency = Counter(words)

for word, frequency in word_frequency.items():
    print(f"{word}:{frequency}")
