animals = [
    {
        "id": 1,
        "name": "Dog",
        "legs": 4,
        "weight": 5.67,
        "height": 4.2,
        "speed": 34,
        "family": 2,
        "image": "path_to_dog_image.jpg"  # Local image path or absolute URL
    },
    {
        "id": 2,
        "name": "Domestic Cat",
        "legs": 2,
        "weight": 5.67,
        "height": 4.2,
        "speed": 34,
        "family": 1,
        "image": "path_to_cat_image.jpg"  # Local image path or absolute URL
    },
    {
        "id": 3,
        "name": "Panther",
        "legs": 2,
        "weight": 5.67,
        "height": 4.2,
        "speed": 34,
        "family": 1,
        "image": "path_to_panther_image.jpg"  # Local image path or absolute URL
    }
    
]
families = [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        }
    ]

def get_all_animals():
    """
    Return information about all the animals, including their family name.
    """
    all_animals = []
    for animal in animals:
        family_id = animal["family"]
        family_name = get_family_name_by_id(family_id)
        animal_info = {
            "id": animal["id"],
            "name": animal["name"],
            "legs": animal["legs"],
            "weight": animal["weight"],
            "height": animal["height"],
            "speed": animal["speed"],
            "family": family_name,
            "image": animal["image"]
        }
        all_animals.append(animal_info)
    return all_animals

def get_all_families():
    """
    Return a list of all the families' names.
    """
    all_family_names = [family["name"] for family in families]
    return all_family_names

def get_one_animal(animal_id):
    """
    Return the information about one animal based on its id.
    """
    animal = next((a for a in animals if a["id"] == animal_id), None)
    if animal:
        family_id = animal["family"]
        family_name = get_family_name_by_id(family_id)
        animal_info = {
            "id": animal["id"],
            "name": animal["name"],
            "legs": animal["legs"],
            "weight": animal["weight"],
            "height": animal["height"],
            "speed": animal["speed"],
            "family": family_name,
            "image": animal["image"]
        }
        return animal_info
    else:
        return None

def get_animals_per_family(family_id):
    """
    Return the information about all the animals from the particular family.
    """
    family_animals = [animal for animal in animals if animal["family"] == family_id]
    family_name = get_family_name_by_id(family_id)
    family_animal_info = []
    for animal in family_animals:
        animal_info = {
            "id": animal["id"],
            "name": animal["name"],
            "legs": animal["legs"],
            "weight": animal["weight"],
            "height": animal["height"],
            "speed": animal["speed"],
            "family": family_name,
            "image": animal["image"]
        }
        family_animal_info.append(animal_info)
    return family_animal_info

def get_family_name_by_id(family_id):
    """
    Return the name of the family based on its id.
    """
    family = next((f for f in families if f["id"] == family_id), None)
    if family:
        return family["name"]
    else:
        return None