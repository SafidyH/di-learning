import json

json_file_path = 'my_folder/file.json'  # Update with the correct path to your file

with open(json_file_path, 'r') as file:
    family = json.load(file)
print("Details about Jane's children:")
for child in family['children']:
    print(f"Child's name: {child['firstName']}")
    print(f"Child's age: {child['age']}")
    print("---------------------------")
favorite_color = 'blue'  # Replace with your desired favorite color

for child in family['children']:
    child['favorite_color'] = favorite_color
with open(json_file_path, 'w') as file:
    json.dump(family, file, indent=4)
