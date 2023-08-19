import json

def is_valid_valentine_item(item):
    words = item.split()
    if len(words) < 2 or not words[0].startswith("V") or any(word.isnumeric() for word in words):
        return False

    first_word, *rest_words = words
    if not all(word[0].islower() for word in rest_words):
        return False

    e_count = sum(word.lower().count("e") for word in words)
    if e_count < 2:
        return False

    try:
        price = float(item.split()[-1].replace(",", "."))
        if not item.endswith(",14") or not (0 <= price <= 99.99):
            return False
    except ValueError:
        return False

    return True

def add_valentine_item(menu_data):
    while True:
        item_name = input("Enter the new Valentine item name: ").strip()
        if is_valid_valentine_item(item_name):
            menu_data["valentine_items"].append({"name": item_name})
            break
        else:
            print("Invalid item name. Please follow the Valentine item rules.")

def display_menu(menu_data):
    print("\nMenu:")
    for item in menu_data["items"]:
        print(f"{item['name']} - ${item['price']}")
    print("\nValentine's Day Specials:")
    for item in menu_data["valentine_items"]:
        print(f"{item['name']} ❤️")

def display_heart():
    print("  ❤️   ❤️  ")
    print(" ❤️ ❤️ ❤️ ❤️ ")
    print("  ❤️ ❤️ ❤️ ")
    print("   ❤️ ❤️ ")
    print("    ❤️ ")
    
def main():
    with open("menu.json", "r") as file:
        menu_data = json.load(file)

    add_valentine_item(menu_data)

    with open("menu.json", "w") as file:
        json.dump(menu_data, file, indent=4)

    display_heart()
    display_menu(menu_data)

if __name__ == "__main__":
    main()
