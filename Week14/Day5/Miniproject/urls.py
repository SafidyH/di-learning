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