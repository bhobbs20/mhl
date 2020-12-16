from django.contrib import admin

from .models import Season, Division, Team, TeamStats, Player, PlayerStats, PlayerGameStats, Game


admin.site.register(Season)
admin.site.register(Division)

admin.site.register(Team)
admin.site.register(TeamStats)
admin.site.register(Game)

admin.site.register(Player)
admin.site.register(PlayerStats)
admin.site.register(PlayerGameStats)




