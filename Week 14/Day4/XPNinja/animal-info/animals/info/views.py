import random
import pronouncing 

from django.shortcuts import render
from .models import Animal, Family

def display_all_animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals/all_animals.html', {'animals': animals})

def display_all_families(request):
    families = Family.objects.all()
    return render(request, 'animals/all_families.html', {'families': families})

def display_one_animal(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animals/animal.html', {'animal': animal})

def display_animal_per_family(request, family_id):
    family = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=family)
    return render(request, 'animals/animals_in_family.html', {'family': family, 'animals': animals})

def create_children_song(request):
    animals = Animal.objects.all()
    families = Family.objects.all()

    animal_names = [animal.name for animal in animals]
    family_names = [family.name for family in families]

    # Generate random rhyming pairs of animals and families
    rhyming_pairs = []
    for animal in animal_names:
        rhymes_with_animal = pronouncing.rhymes(animal)
        for family in family_names:
            if any(family.lower() in rhyme for rhyme in rhymes_with_animal):
                rhyming_pairs.append((animal, family))

    # Shuffle the rhyming pairs to make the song random
    random.shuffle(rhyming_pairs)

    # Construct the song
    song_lines = []
    for animal, family in rhyming_pairs:
        song_lines.append(f"Little {animal} from the {family} family,")
        song_lines.append("Jumped around so happily.")
        song_lines.append("With a hop, skip, and a jump,")
        song_lines.append("They played all day without a thump.")

    song = "\n".join(song_lines)

    return render(request, 'animals/song.html', {'song': song})