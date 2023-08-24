from django.shortcuts import render
from .data import animals, families
import json
from .read_data import get_all_animals, get_all_families, get_one_animal, get_animals_per_family


def display_all_animals(request):
    #context = {'animals': animals}
    animals_info = get_all_animals()
    #return render(request, 'animals/all_animals.html', context)
    return render(request, 'animals/all_animals.html', {'animals': animals})
    

def display_all_families(request):
    #context = {'families': families}
    families = get_all_families()
    #return render(request, 'animals/all_families.html', context)
    return render(request, 'animals/all_families.html', {'families': families})

def display_one_animal(request, animal_id):
    #animal = next((a for a in animals if a['id'] == animal_id), None)
    animal_info = get_one_animal(animal_id)
    if animal_info:
        return render(request, 'animals/animal.html', {'animal_info': animal_info})
    else:
        return render(request, 'animals/animal_not_found.html')
    #if animal:
        #context = {'animal': animal}
        #return render(request, 'animals/animal.html', context)
    #else:
        #return render(request, '404.html')  # Handle not found

def display_animal_per_family(request, family_id):
    #animals_in_family = [a for a in animals if a['family'] == family_id]
    #family = next((f for f in families if f['id'] == family_id), None)
    #if family:
        #context = {'animals_in_family': animals_in_family, 'family': family}
        #return render(request, 'animals/animals_in_family.html', context)
    #else:
        #return render(request, '404.html')  # Handle not found
    
    animals_in_family = get_animals_per_family(family_id)
    if animals_in_family:
        return render(request, 'animals/animals_in_family.html', {'animals_in_family': animals_in_family})
    else:
        return render(request, 'animals/family_not_found.html')

def read_json_file(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def get_all_animals():
    data = read_json_file('animals_data.json')
    animals_info = []
    for animal in data['animals']:
        family_name = next((family['name'] for family in data['families'] if family['id'] == animal['family']), '')
        animal_info = {
            'id': animal['id'],
            'name': animal['name'],
            'legs': animal['legs'],
            'weight': animal['weight'],
            'height': animal['height'],
            'speed': animal['speed'],
            'family_name': family_name
        }
        animals_info.append(animal_info)
    return animals_info

def get_all_families():
    data = read_json_file('animals_data.json')
    return data['families']

def get_one_animal(animal_id):
    data = read_json_file('animals_data.json')
    animal = next((a for a in data['animals'] if a['id'] == animal_id), None)
    if animal:
        family_name = next((family['name'] for family in data['families'] if family['id'] == animal['family']), '')
        animal_info = {
            'id': animal['id'],
            'name': animal['name'],
            'legs': animal['legs'],
            'weight': animal['weight'],
            'height': animal['height'],
            'speed': animal['speed'],
            'family_name': family_name
        }
        return animal_info
    else:
        return None

def get_animals_per_family(family_id):
    data = read_json_file('animals_data.json')
    animals_in_family = []
    family = next((f for f in data['families'] if f['id'] == family_id), None)
    if family:
        for animal in data['animals']:
            if animal['family'] == family_id:
                animal_info = {
                    'id': animal['id'],
                    'name': animal['name'],
                    'legs': animal['legs'],
                    'weight': animal['weight'],
                    'height': animal['height'],
                    'speed': animal['speed'],
                    'family_name': family['name']
                }
                animals_in_family.append(animal_info)
        return animals_in_family
    else:
        return None