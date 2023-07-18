import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        bark_output = self.bark()
        self.trained = True
        return bark_output

    def play(self, *args):
        dog_names = ', '.join(args)
        return f'{dog_names} all play together'

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f'{self.name} does a barrel roll',
                f'{self.name} stands on his back legs',
                f'{self.name} shakes your hand',
                f'{self.name} plays dead'
            ]
            return random.choice(tricks)
        else:
            return f'{self.name} is not trained to do tricks'

dog1 = PetDog("Max", 3, 15)
dog2 = PetDog("Bella", 4, 20)

print(dog1.train())  # Max is barking
print(dog1.trained)  # True

print(dog2.play("Charlie", "Lucy"))  # Charlie, Lucy all play together

print(dog1.do_a_trick())  # Max stands on his back legs
print(dog2.do_a_trick())  # Bella is not trained to do tricks
