import random

def hangman():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    word = random.choice(wordslist)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        # Display the current state of the word with asterisks for unknown letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "*"
        print(display_word)

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess has already been made
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
            print("Attempts remaining:", attempts)

        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if attempts == 0:
        print("Game over! You ran out of attempts. The word was:", word)

# Start the game
hangman()
