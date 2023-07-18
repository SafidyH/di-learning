birthdays = {
    "Alice": "1990/05/15",
    "Bob": "1985/12/03",
    "Charlie": "1998/08/20",
    "David": "1993/02/10",
    "Emma": "1996/11/25"
}

print("Welcome to the Birthday Look-Up!")
print("You can look up the birthdays of the people in the list!")
print("Names in the dictionary:")
for name in birthdays:
    print(name)

person = input("Enter a person's name: ")

if person in birthdays:
    birthday = birthdays[person]
    print(f"The birthday of {person} is {birthday}")
else:
    print(f"Sorry, we don't have the birthday information for {person}.")

add_new = input("Do you want to add a new birthday? (yes/no): ")

if add_new.lower() == "yes":
    new_person = input("Enter the person's name: ")
    new_birthday = input("Enter the person's birthday (YYYY/MM/DD): ")
    birthdays[new_person] = new_birthday
    print(f"{new_person}'s birthday has been added to the dictionary.")

print("Updated names in the dictionary:")
for name in birthdays:
    print(name)
