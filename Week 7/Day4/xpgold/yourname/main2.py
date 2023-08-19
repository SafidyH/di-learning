def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"

    return full_name

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name (optional): ")
    last_name = input("Enter your last name: ")

    full_name = get_full_name(first_name, last_name, middle_name)

    print(f"Your full name is: {full_name}")
def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"

    return full_name

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name (optional): ")
    last_name = input("Enter your last name: ")

    full_name = get_full_name(first_name, last_name, middle_name)

    print(f"Your full name is: {full_name}")
