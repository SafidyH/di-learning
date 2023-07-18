total_cost = 0
num_people = int(input("Enter the number of people in the family: "))

for _ in range(num_people):
    age = int(input("Enter the age of a person: "))
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price

print("Total cost for the family:", total_cost)

teenagers = ["John", "Emily", "Michael", "Sarah", "David"]
allowed_ages = []

for teenager in teenagers:
    age = int(input(f"Enter the age of {teenager}: "))
    if 16 <= age <= 21:
        allowed_ages.append(teenager)

print("Teenagers allowed to watch the movie:", allowed_ages)
