from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.teams, name='teams'),
    path('players/', views.player_stats, name='players_stats'),
    path('standings/', views.standings, name='standings'),
    path('schedule/', views.league_schedule, name='schedule'),
]