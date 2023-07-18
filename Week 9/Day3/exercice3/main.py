import os

# Create a folder
folder_name = 'my_folder'
os.makedirs(folder_name)

# Save code into the JSON file
code = '''
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
'''
json_file_path = os.path.join(folder_name, 'file.json')
with open(json_file_path, 'w') as file:
    file.write(code)

# Create an empty index.py file
index_file_path = os.path.join(folder_name, 'index.py')
open(index_file_path, 'a').close()

print("Folder and files created successfully.")
