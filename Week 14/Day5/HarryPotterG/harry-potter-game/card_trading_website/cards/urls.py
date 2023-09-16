from django.urls import path
from . import views
from cards import views as cards_views


urlpatterns = [
    path('cards/', views.display_all_cards, name='display_all_cards'),
    path('cards/', cards_views.display_all_cards, name='display_all_cards'),
    path('card/<int:card_id>/', views.display_one_card, name='display_one_card'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('buy/<int:card_id>/<int:user_id>/', views.buy_one_card, name='buy_one_card'),
    path('sell/<int:card_id>/<int:user_id>/', views.sell_one_card, name='sell_one_card'),
]
