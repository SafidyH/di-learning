from django.db import models
import requests
import random

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    amount_of_money = models.DecimalField(default=1000, max_digits=10, decimal_places=2)
    points = models.PositiveIntegerField(default=0)

class Card(models.Model):
    name_character = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    house = models.CharField(max_length=100)
    image_url = models.URLField()
    date_of_birth = models.DateField()
    patronus = models.CharField(max_length=100)
    price = models.DecimalField(default=200, max_digits=6, decimal_places=2)
    xp_points = models.PositiveIntegerField(default=1)
    current_owner = models.ForeignKey(User, related_name='owned_cards', null=True, blank=True, on_delete=models.SET_NULL)
    previous_owner = models.ForeignKey(User, related_name='sold_cards', null=True, blank=True, on_delete=models.SET_NULL)

def populate_cards():
    url = "https://api.example.com/harrypotter/cards"  # Replace with the actual Harry Potter API endpoint
    response = requests.get(url)
    cards_data = response.json()

    user, created = User.objects.get_or_create(username='default_user', email='user@example.com')

    for card_data in cards_data:
        card = Card(
            name_character=card_data['name'],
            species=card_data['species'],
            house=card_data['house'],
            image_url=card_data['image_url'],
            date_of_birth=card_data['date_of_birth'],
            patronus=card_data['patronus'],
            price=random.randint(200, 2000),
            xp_points=random.randint(1, 10),
            current_owner=None,
            previous_owner=None,
        )
        card.save()
