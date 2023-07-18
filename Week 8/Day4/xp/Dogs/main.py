class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} won the fight'
        else:
            return f'{other_dog.name} won the fight'

dog1 = Dog("Max", 3, 15)
dog2 = Dog("Bella", 4, 20)
dog3 = Dog("Charlie", 2, 12)

print(dog1.bark())  # Max is barking
print(dog2.run_speed())  # 5.0
print(dog3.fight(dog2))  # Bella won the fight
