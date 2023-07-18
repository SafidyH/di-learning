birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1985/12/03",
    "Charlie": "1998/08/20",
    "David": "1993/02/10",
    "Emma": "1996/11/25"
}

print("Welcome to the Birthday Look-Up!")
print("You can look up the birthdays of the people in the list!")

person = input("Enter a person's name: ")

birthday = birthdays.get(person)

if birthday:
    print(f"The birthday of {person} is {birthday}")
else:
    print(f"Sorry, the birthday of {person} is not available in the list.")
