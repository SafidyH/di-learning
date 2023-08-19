def sort_words_alphabetically(input_string):
    words = [word.strip() for word in input_string.split(",")]
    sorted_words = sorted(words)
    return ",".join(sorted_words)

if __name__ == "__main__":
    input_sequence = input("Enter comma-separated words: ")
    result = sort_words_alphabetically(input_sequence)
    print("Sorted words:", result)
