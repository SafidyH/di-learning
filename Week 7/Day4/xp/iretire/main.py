from datetime import datetime

def get_age(year, month, day):
    current_date = datetime.now()
    age = current_date.year - year

    if current_date.month < month:
        age -= 1
    elif current_date.month == month and current_date.day < day:
        age -= 1

    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)

    if gender == 'm':
        return age >= 67
    elif gender == 'f':
        return age >= 62 and year > 1947

    return False

gender = input("Enter your gender (m/f): ")
date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")

retirement_eligible = can_retire(gender, date_of_birth)
if retirement_eligible:
    print("You can retire!")
else:
    print("You are not eligible for retirement yet.")
