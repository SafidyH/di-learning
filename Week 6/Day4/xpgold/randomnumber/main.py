import random

games_won = 0
games_lost = 0

while True:
    user_input = input("Guess a number from 1 to 9 (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    random_number = random.randint(1, 9)

    if int(user_input) == random_number:
        print("Winner!")
        games_won += 1
    else:
        print("Better luck next time!")
        games_lost += 1

print(f"Total games won: {games_won}")
print(f"Total games lost: {games_lost}")
