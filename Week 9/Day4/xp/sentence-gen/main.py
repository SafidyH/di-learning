import random

def get_words_from_file(filename):
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words_list):
    if length < 2 or length > 20:
        raise ValueError("Length should be an integer between 2 and 20.")
    random_words = random.sample(words_list, length)
    sentence = " ".join(random_words)
    return sentence.lower()

def main():
    print("Random Sentence Generator")
    words_list = get_words_from_file("words.txt")
    
    try:
        sentence_length = int(input("Enter the length of the sentence (2 to 20): "))
        sentence = get_random_sentence(sentence_length, words_list)
        print("Generated Sentence:", sentence)
    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")

if __name__ == "__main__":
    main()
