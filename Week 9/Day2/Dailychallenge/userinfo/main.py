# Ask the user for inputs and create a list of tuples
data = []
for _ in range(5):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    score = int(input("Enter Score: "))
    data.append((name, age, score))

# Sort the list of tuples based on Name > Age > Score
data.sort(key=lambda x: (x[0], x[1], x[2]))

print(data)
