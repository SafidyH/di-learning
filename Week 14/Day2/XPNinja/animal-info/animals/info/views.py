from django.shortcuts import render
from django.http import HttpResponse
from .animal_class import Animal

def add_animal_view(request):
    name = request.GET.get('name')
    legs = int(request.GET.get('legs'))
    weight = float(request.GET.get('weight'))
    height = float(request.GET.get('height'))
    speed = float(request.GET.get('speed'))
    family = int(request.GET.get('family'))

    Animal.add_animal(name, legs, weight, height, speed, family)

    return HttpResponse("Animal added successfully.")

