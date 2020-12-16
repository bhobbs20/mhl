from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=200, unique=True)
    season_number = models.IntegerField()

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    logo = models.ImageField(upload_to='teams/%Y/%m/%d/')
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TeamStats(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    wins = models.IntegerField(null=True, blank=True)
    loss = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    goals_scored = models.IntegerField(null=True, blank=True)
    goals_against = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.team.name + ' ' + self.season.name


class Player(models.Model):
    features_choices = (
        ('g', 'goalie'),
        ('f', 'forward'),
        ('d', 'defense'),
    )
    team = models.ForeignKey(Team,  on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    position = models.CharField(choices=features_choices, max_length=50)

    def __str__(self):
        return self.first_name + ' ' +  self.last_name


class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    gaa = models.IntegerField(default=0)

    def __str__(self):
        return self.player.first_name + ' ' + self.player.last_name


class Game(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.home_team.name + ' vs ' + self.away_team.name


class PlayerGameStats(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    gaa = models.IntegerField(default=0)

    def __str__(self):
        return self.player.last_name + ' ' + self.game.home_team.name + ' vs ' + self.game.away_team.name



