# card_trading_website/settings.py
# Assurez-vous d'ajouter les configurations appropriées pour PostgreSQL.

# cards/models.py
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

# cards/admin.py
from django.contrib import admin
from .models import User, Card

admin.site.register(User)
admin.site.register(Card)

# cards/views.py
from django.shortcuts import render
from .models import Card, User

def display_all_cards(request):
    cards = Card.objects.filter(current_owner__isnull=True)
    return render(request, 'cards/cards.html', {'cards': cards})

def display_one_card(request, card_id):
    card = Card.objects.get(pk=card_id)
    return render(request, 'cards/card_detail.html', {'card': card})

def user_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'cards/user_profile.html', {'user': user})

def buy_one_card(request, card_id, user_id):
    card = Card.objects.get(pk=card_id)
    user = User.objects.get(pk=user_id)

    if user.amount_of_money >= card.price:
        user.amount_of_money -= card.price
        user.points += card.xp_points
        card.previous_owner = card.current_owner
        card.current_owner = user
        card.save()
        user.save()

    return render(request, 'cards/buy_card.html', {'card': card, 'user': user})

def sell_one_card(request, card_id, user_id):
    card = Card.objects.get(pk=card_id)
    user = User.objects.get(pk=user_id)

    if card.current_owner == user:
        user.points -= card.xp_points
        card.previous_owner = card.current_owner
        card.current_owner = None
        card.save()
        user.save()

    return render(request, 'cards/sell_card.html', {'card': card, 'user': user})

# card_trading_website/urls.py
from django.contrib import admin
from django.urls import path, include
from cards.views import display_all_cards, display_one_card, user_profile, buy_one_card, sell_one_card

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', display_all_cards, name='display_all_cards'),
    path('cards/<int:card_id>/', display_one_card, name='display_one_card'),
    path('profile/<int:user_id>/', user_profile, name='user_profile'),
    path('cards/<int:card_id>/buy/<int:user_id>/', buy_one_card, name='buy_one_card'),
    path('cards/<int:card_id>/sell/<int:user_id>/', sell_one_card, name='sell_one_card'),
]

# cards/templates/cards/cards.html
#<!-- Template for displaying all cards available in the market to buy -->
#{% for card in cards %}
#    <!-- Display card details -->
#{% endfor %}

# cards/templates/cards/card_detail.html
#<!-- Template for displaying a specific card's detailed information -->
#<!-- Display card details -->

# cards/templates/cards/user_profile.html
#<!-- Template for displaying a user's profile and the cards they own -->
#<!-- Display user details and owned cards -->

# cards/templates/cards/buy_card.html
#<!-- Template for displaying the result of buying a card -->
#<!-- Display purchase success or failure message -->

# cards/templates/cards/sell_card.html
#<!-- Template for displaying the result of selling a card -->
#<!-- Display sell success or failure message -->
