from django.urls import path
from .views import *
from django.urls import include


urlpatterns = [
    path('get_new_slider/', get_new_slider),
    path('get_video/', get_video),
    path('get_players/', get_players),
    path('get_shop/', get_shop),
    path('get_information/', get_information),
    path('get_partners/', get_partners),
    path('get_news/', get_news),
    path('get_club/', get_club),
    path('get_academy/', get_academy),
    path('get_arena/', get_arena),
    path('get_background/', get_background),
    path('delete-players/<int:pk>/', delete_players_view),
]


