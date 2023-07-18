family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    
    print(f"{name} has to pay ${ticket_price}")
    total_cost += ticket_price

print(f"Total cost for the movies: ${total_cost}")

family = {}

num_family_members = int(input("Enter the number of family members: "))

for _ in range(num_family_members):
    name = input("Enter the name of a family member: ")
    age = int(input("Enter the age of the family member: "))
    family[name] = age

