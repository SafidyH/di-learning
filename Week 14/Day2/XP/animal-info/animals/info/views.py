from django.shortcuts import render
from .data import animals, families

def display_all_animals(request):
    context = {'animals': animals}
    return render(request, 'animals/all_animals.html', context)

def display_all_families(request):
    context = {'families': families}
    return render(request, 'animals/all_families.html', context)

def display_one_animal(request, animal_id):
    animal = next((a for a in animals if a['id'] == animal_id), None)
    if animal:
        context = {'animal': animal}
        return render(request, 'animals/animal.html', context)
    else:
        return render(request, '404.html')  # Handle not found

def display_animal_per_family(request, family_id):
    animals_in_family = [a for a in animals if a['family'] == family_id]
    family = next((f for f in families if f['id'] == family_id), None)
    if family:
        context = {'animals_in_family': animals_in_family, 'family': family}
        return render(request, 'animals/animals_in_family.html', context)
    else:
        return render(request, '404.html')  # Handle not found
