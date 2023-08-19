class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    def basic_attack(self, other_character):
        other_character.life -= self.attack

class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Druid {self.name} is created!")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other_character):
        other_character.life -= int(0.75 * self.life + 0.75 * self.attack)

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Warrior {self.name} is created!")

    def brawl(self, other_character):
        other_character.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        self.attack += 2
        self.life += 2

    def roar(self, other_character):
        other_character.attack -= 3

class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"Mage {self.name} is created!")

    def curse(self, other_character):
        other_character.attack -= 2

    def summon(self):
        self.attack += 3

    def cast_spell(self, other_character):
        other_character.life -= int(self.attack / 5)

# Testing the classes
if __name__ == "__main__":
    druid = Druid("Alistair")
    warrior = Warrior("Thrain")
    mage = Mage("Eldora")

    druid.meditate()
    warrior.train()
    mage.summon()

    druid.basic_attack(warrior)
    warrior.roar(mage)
    mage.cast_spell(druid)

    print("After the attacks:")
    print(f"{warrior.name} - Life: {warrior.life}, Attack: {warrior.attack}")
    print(f"{druid.name} - Life: {druid.life}, Attack: {druid.attack}")
    print(f"{mage.name} - Life: {mage.life}, Attack: {mage.attack}")
