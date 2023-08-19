def get_age(year, month, day):
    current_year = 2023  # Replace this with the current year
    current_month = 7    # Replace this with the current month

    age = current_year - year

    # Adjust age based on birth month
    if month > current_month:
        age -= 1

    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)

    if gender.lower() == "m":
        retirement_age = 67
    elif gender.lower() == "f" and year > 1947 and (year != 1947 or month >= 4):
        retirement_age = 62
    else:
        return False  # Invalid gender or birth date

    return age >= retirement_age

if __name__ == "__main__":
    gender = input("Enter your gender (m/f): ")
    date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")

    if can_retire(gender, date_of_birth):
        print("Congratulations! You can retire.")
    else:
        print("Sorry, you cannot retire yet.")
