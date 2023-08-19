from menu_manager import MenuManager

def load_manager():
    return MenuManager()

def show_user_menu():
    print("Menu Options:")
    print("1. Add Item to Menu")
    print("2. Remove Item from Menu")
    print("3. Show Restaurant Menu")
    print("4. Exit")

def add_item_to_menu(manager):
    name = input("Enter the item's name: ")
    price = float(input("Enter the item's price: "))
    manager.add_item(name, price)
    print("Item was added successfully.")

def remove_item_from_menu(manager):
    name = input("Enter the item's name to remove: ")
    if manager.remove_item(name):
        print("Item was deleted successfully.")
    else:
        print("Error: Item not found.")

def show_restaurant_menu(manager):
    print("\nRestaurant Menu:")
    for item in manager.menu:
        print(f"{item['name']}: ${item['price']}")

def main():
    manager = load_manager()

    while True:
        show_user_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item_to_menu(manager)
        elif choice == "2":
            remove_item_from_menu(manager)
        elif choice == "3":
            show_restaurant_menu(manager)
        elif choice == "4":
            manager.save_to_file()
            print("Menu was saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    print("Exercise Menu Manager")
    main()
