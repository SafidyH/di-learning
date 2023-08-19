import json

class MenuManager:
    def __init__(self):
        self.menu = self.load_menu()

    def load_menu(self):
        with open("restaurant_menu.json", "r") as file:
            menu_data = json.load(file)
        return menu_data["items"]

    def add_item(self, name, price):
        self.menu.append({"name": name, "price": price})

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                return True
        return False

    def save_to_file(self):
        with open("restaurant_menu.json", "w") as file:
            json.dump({"items": self.menu}, file, indent=4)
