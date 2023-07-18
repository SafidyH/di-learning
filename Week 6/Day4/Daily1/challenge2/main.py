word = input("Enter a word: ")

new_word = ""
prev_letter = ""

for letter in word:
    if letter != prev_letter:
        new_word += letter
        prev_letter = letter

print(new_word)
