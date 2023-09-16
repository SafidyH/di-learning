from django.shortcuts import render
from .models import Animal, Family

#def display_all_animals(request):
    #animals = Animal.objects.all()
    #return render(request, 'animals/all_animals.html', {'animals': animals})

#def display_all_families(request):
    #families = Family.objects.all()
    #return render(request, 'animals/all_families.html', {'families': families})

#def display_one_animal(request, animal_id):
    #animal = Animal.objects.get(id=animal_id)
    #return render(request, 'animals/animal.html', {'animal': animal})

#def display_animal_per_family(request, family_id):
    #family = Family.objects.get(id=family_id)
    #animals = Animal.objects.filter(family=family)
    #return render(request, 'animals/animals_in_family.html', {'family': family, 'animals': animals})

def display_all_animals(request):
    animals = Animal.objects.all().order_by('name')
    return render(request, 'animal_list.html', {'animals': animals})

def display_all_families(request):
    families = Family.objects.all().order_by('id')
    return render(request, 'family_list.html', {'families': families})

def display_one_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})

def display_animal_per_family(request, family_id):
    family = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=family)
    num_animals = animals.count()
    return render(request, 'animals_in_family.html', {'family': family, 'animals': animals, 'num_animals': num_animals})

def display_animal_by_speed(request):
    animals = Animal.objects.all().order_by('speed')
    return render(request, 'animal_list.html', {'animals': animals})