import requests

def get_chuck_norris_jokes(category):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        joke_data = response.json()  # Parse the JSON response
        joke = joke_data["value"]
        return joke
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None
    except KeyError:
        print("Invalid category or no jokes found in the category.")
        return None

def main():
    categories = ["animal", "career", "celebrity", "dev", "explicit", "fashion", "food",
                  "history", "money", "movie", "music", "political", "religion", "science",
                  "sport", "travel"]

    # Ask the user to choose a category
    print("Available categories:")
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")
    
    category_choice = int(input("Enter the number corresponding to the category you want: ")) - 1
    if 0 <= category_choice < len(categories):
        chosen_category = categories[category_choice]
        joke = get_chuck_norris_jokes(chosen_category)
        if joke:
            print("Chuck Norris Joke:", joke)
    else:
        print("Invalid category choice.")

if __name__ == "__main__":
    main()
