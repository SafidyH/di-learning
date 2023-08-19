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
