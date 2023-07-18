class AnagramChecker:
    def __init__(self, wordlist_file):
        with open(wordlist_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file.readlines())

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for entry in self.word_list:
            if self.is_anagram(word, entry) and entry != word:
                anagrams.append(entry)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())


from anagram_checker import AnagramChecker

def validate_input(word):
    if len(word.split()) != 1:
        print("Error: Only a single word is allowed.")
        return False
    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False
    return True

def display_anagrams(word, anagrams):
    print("YOUR WORD: '{}'".format(word))
    if anagrams:
        print("This is a valid English word.")
        print("Anagrams for your word: {}".format(", ".join(anagrams)))
    else:
        print("This is a valid English word, but it has no anagrams.")

def main():
    wordlist_file = "wordlist.txt"  # Replace with the path to your word list file
    anagram_checker = AnagramChecker(wordlist_file)

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            word = input("Enter a word: ").strip()
            if validate_input(word):
                anagrams = anagram_checker.get_anagrams(word)
                display_anagrams(word, anagrams)
        elif choice == "2":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
