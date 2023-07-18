longest_sentence = ""
congratulations_message = "Congratulations! You set a new longest sentence without the character 'A'."

while True:
    sentence = input("Enter the longest sentence without the character 'A' (or enter 'q' to quit): ")

    if sentence == "q":
        break

    if "A" not in sentence and len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        print(congratulations_message)

print("Longest sentence without the character 'A':", longest_sentence)
