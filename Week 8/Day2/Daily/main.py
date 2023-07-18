class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        info = f"{self.farm_name}'s farm\n\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "\nE-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_types_str = ', '.join(animal_types)
        return f"{self.farm_name}'s farm has {animal_types_str}."


# Example usage
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

animal_types = macdonald.get_animal_types()
print(animal_types)

short_info = macdonald.get_short_info()
print(short_info)
