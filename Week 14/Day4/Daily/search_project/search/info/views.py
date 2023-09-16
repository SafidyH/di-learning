from django.shortcuts import render

from .models import Person

def search_person_by_phonenumber(request, phonenumber):
    try:
        person = Person.objects.get(phone_number=phonenumber)
    except Person.DoesNotExist:
        person = None

    return render(request, 'person_detail.html', {'person': person})

def search_persons_by_name(request, name):
    persons = Person.objects.filter(name__icontains=name)
    return render(request, 'persons_list.html', {'persons': persons})

def display_person_by_phonenumber(request, number):
    try:
        person = Person.objects.get(phone_number=number)
    except Person.DoesNotExist:
        person = None

    return render(request, 'person_by_number.html', {'person': person})

def display_person_by_name(request, name):
    persons = Person.objects.filter(name__icontains=name)
    return render(request, 'person_by_name.html', {'persons': persons})
