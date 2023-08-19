import random
import json

class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()

    def roll_dice(self):
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.remove(min(dice))
        return sum(dice)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }


class Game:
    def __init__(self):
        self.players = []

    def create_characters(self):
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            name = input(f"Enter the name of player {i + 1}: ")
            age = int(input(f"Enter the age of player {i + 1}: "))
            character = Character(name, age)
            self.players.append(character)

    def export_to_txt(self):
        with open("characters.txt", "w") as file:
            for player in self.players:
                file.write(f"{player.name} (Age: {player.age})\n")
                file.write(f"Strength: {player.strength}\n")
                file.write(f"Dexterity: {player.dexterity}\n")
                file.write(f"Constitution: {player.constitution}\n")
                file.write(f"Intelligence: {player.intelligence}\n")
                file.write(f"Wisdom: {player.wisdom}\n")
                file.write(f"Charisma: {player.charisma}\n\n")

    def export_to_json(self):
        data = [player.to_dict() for player in self.players]
        with open("characters.json", "w") as file:
            json.dump(data, file, indent=4)


def main():
    game = Game()
    game.create_characters()
    game.export_to_txt()
    game.export_to_json()


if __name__ == "__main__":
    main()
