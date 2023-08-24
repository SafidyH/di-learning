from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    print("Menu:")
    print("View an Item (V)")
    print("Add an Item (A)")
    print("Delete an Item (D)")
    print("Update an Item (U)")
    print("Show the Menu (S)")
    choice = input("Enter your choice: ").upper()
    if choice == 'V':
        item_name = input("Enter the item name: ")
        item = MenuManager.get_by_name(item_name)
        if item:
            print(f"Item: {item.item_name}, Price: {item.item_price}")
        else:
            print("Item not found.")
    elif choice == 'A':
        add_item_to_menu()
    elif choice == 'D':
        remove_item_from_menu()
    elif choice == 'U':
        update_item_from_menu()
    elif choice == 'S':
        show_restaurant_menu()
    else:
        print("Invalid choice. Try again.")

def add_item_to_menu():
    item_name = input("Enter the item name: ")
    item_price = int(input("Enter the item price: "))
    item = MenuItem(item_name, item_price)
    item.save()

def remove_item_from_menu():
    item_name = input("Enter the name of the item to remove: ")
    item = MenuItem(item_name, 0)
    item.delete()

def update_item_from_menu():
    item_name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name: ")
    new_price = int(input("Enter the new price: "))
    item = MenuItem(item_name, 0)
    item.update(new_name, new_price)

def show_restaurant_menu():
    items = MenuManager.all_items()
    for item in items:
        print(f"Item: {item.item_name}, Price: {item.item_price}")

def main():
    while True:
        show_user_menu()
        exit_choice = input("Do you want to exit? (Y/N): ").upper()
        if exit_choice == 'Y':
            show_restaurant_menu()
            break

if __name__ == "__main__":
    main()
