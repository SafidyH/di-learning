def count_occurrences(string, character):
    count = string.count(character)
    return count

string = "Programming is cool!"
character = "o"
occurrences = count_occurrences(string, character)
print(f"The character '{character}' occurs {occurrences} times in the string.")

string = "This is a great example"
character = "y"
occurrences = count_occurrences(string, character)
print(f"The character '{character}' occurs {occurrences} times in the string.")
