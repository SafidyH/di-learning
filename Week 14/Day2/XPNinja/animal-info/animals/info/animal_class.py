import json

class Animal:
    def __init__(self, name, legs, weight, height, speed, family):
        self.name = name
        self.legs = legs
        self.weight = weight
        self.height = height
        self.speed = speed
        self.family = family

    @classmethod
    def add_animal(cls, name, legs, weight, height, speed, family):
        # Load existing data from JSON file
        with open('animals.json', 'r') as file:
            data = json.load(file)
        
        # Find the next available ID
        next_id = max([animal['id'] for animal in data]) + 1 if data else 1
        
        # Create a new animal dictionary
        new_animal = {
            'id': next_id,
            'name': name,
            'legs': legs,
            'weight': weight,
            'height': height,
            'speed': speed,
            'family': family
        }
        
        # Add the new animal to the data
        data.append(new_animal)
        
        # Write the updated data back to JSON file
        with open('animals.json', 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def get_animals(cls):
        # Load animal data from JSON file
        with open('animals.json', 'r') as file:
            data = json.load(file)
        return data
