from django.shortcuts import render
from .models import Animal, Family

def display_all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'all_animals.html', {'animals': animals})

def display_all_families(request):
    families = Family.objects.all()
    return render(request, 'all_families.html', {'families': families})

def display_one_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'animal': animal})

def display_animal_per_family(request, family_id):
    family = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'animals_in_family.html', {'family': family, 'animals': animals})

