from django.shortcuts import render
from .models import PlayerStats, TeamStats, Game


def teams(request):
    east_teams = TeamStats.objects.filter(team__division__name='East')
    west_teams = TeamStats.objects.filter(team__division__name='West')
    context = {
        'east_teams': east_teams,
        'west_teams': west_teams,
    }
    return render(request, 'mhl/teams.html', context)


def player_stats(request):
    all_players = PlayerStats.objects.all().order_by('-player__playerstats__points')

    context = {
        'all_players': all_players,
    }

    return render(request, 'mhl/player_stats.html', context)


def standings(request):
    all_teams = TeamStats.objects.all().order_by('team__teamstats__points')
    east_teams = TeamStats.objects.filter(team__division__name='East').order_by('team__teamstats__points')
    west_teams = TeamStats.objects.filter(team__division__name='West').order_by('team__teamstats__points')

    context = {
        'all_teams': all_teams,
        'east_teams': east_teams,
        'west_teams': west_teams,
    }
    return render(request, 'mhl/standings.html', context)


def league_schedule(request):
    league_games = Game.objects.all()

    context = {
        'league_games': league_games,
    }

    return render(request, 'mhl/schedule.html', context)

