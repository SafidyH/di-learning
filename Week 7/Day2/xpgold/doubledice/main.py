import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        count += 1
        if dice1 == dice2:
            return count

def main():
    throws = []
    for _ in range(100):
        throws.append(throw_until_doubles())

    total_throws = sum(throws)
    average_throws = total_throws / len(throws)

    print("Total throws:", total_throws)
    print("Average throws to reach doubles:", round(average_throws, 2))

# Call the main function
main()
