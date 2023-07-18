class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family! A new child has been born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        first_names = [member['name'] for member in self.members]
        print(f"Family: {self.last_name}")
        print("Members: " + ", ".join(first_names))


# Example usage:
family = Family("Smith")
family.born(name="John", age=5, gender="Male", is_child=True)
family.born(name="Emily", age=28, gender="Female", is_child=False)

print(family.is_18("John"))  # False
print(family.is_18("Sarah"))  # True

family.family_presentation()
