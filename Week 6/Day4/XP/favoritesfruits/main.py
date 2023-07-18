favorite_fruits = input("Enter your favorite fruit(s), separated by a space: ").split()

chosen_fruit = input("Enter a fruit name: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")
