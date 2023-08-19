def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

if __name__ == "__main__":
    input_string = input("Enter the string: ")
    character = input("Enter the character to count: ")

    if len(character) != 1:
        print("Please enter a single character.")
    else:
        result = count_occurrences(input_string, character)
        print(f"Number of occurrences of '{character}' in the string: {result}")
