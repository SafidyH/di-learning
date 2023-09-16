#from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Card

def display_all_cards(request):
    available_cards = Card.objects.filter(current_owner=None)
    context = {'available_cards': available_cards}
    return render(request, 'cards/display_all_cards.html', context)

def display_one_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, 'cards/display_one_card.html', {'card': card})

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_cards = Card.objects.filter(current_owner=user)
    context = {'user_profile': user, 'user_cards': user_cards}
    return render(request, 'cards/user_profile.html', context)

def buy_one_card(request, card_id, user_id):
    card = get_object_or_404(Card, id=card_id)
    user = get_object_or_404(User, id=user_id)

    if user.amount_of_money >= card.price:
        card.previous_owner = card.current_owner
        card.current_owner = user
        card.current_owner.points += card.xp_points
        card.current_owner.amount_of_money -= card.price
        card.current_owner.save()
        card.save()

    return redirect('display_all_cards')  # Redirect back to the list of available cards

def sell_one_card(request, card_id, user_id):
    card = get_object_or_404(Card, id=card_id)
    user = get_object_or_404(User, id=user_id)

    if card.current_owner == user:
        card.previous_owner = user
        card.current_owner = None
        card.current_owner.points -= card.xp_points
        card.current_owner.save()
        card.save()

    return redirect('user_profile', user_id=user_id)  # Redirect back to the user's profile page
