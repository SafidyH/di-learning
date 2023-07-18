class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        new_item = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten,
        }
        self.menu.append(new_item)
        print(f"Added {name} to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"Updated {name} in the menu.")
                break
        else:
            print(f"{name} is not in the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] == name:
                self.menu.remove(dish)
                print(f"Removed {name} from the menu.")
                break
        else:
            print(f"{name} is not in the menu.")

    def print_menu(self):
        print("Menu:")
        for dish in self.menu:
            print(
                f"Name: {dish['name']}, Price: {dish['price']}, Spice: {dish['spice']}, Gluten: {dish['gluten']}"
            )


# Example usage
manager = MenuManager()
manager.print_menu()

manager.add_item("Pizza", 20, "B", True)
manager.print_menu()

manager.update_item("Salad", 22, "B", False)
manager.print_menu()

manager.remove_item("Soup")
manager.print_menu()
