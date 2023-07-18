class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
        ]

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} can use their power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredible Names and Powers:")
        for member in self.members:
            print(f"{member['incredible_name']}: {member['power']}")


# Example usage:
incredibles = TheIncredibles("Incredibles")
incredibles.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power")

incredibles.incredible_presentation()

try:
    incredibles.use_power("Baby Jack")
except Exception as e:
    print(e)

incredibles.use_power("Sarah")
