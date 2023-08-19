import json

sampleJson = """{
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""

# Load the JSON-string as a Python dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Add a new key "birth_date"
data["company"]["employee"]["birth_date"] = "1990-01-01"

# Save the modified dictionary as JSON to a file
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON data with birth_date added saved to modified_data.json.")
