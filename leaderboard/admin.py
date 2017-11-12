from django.contrib import admin
from .models import Leaderboard

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'type', 'numGames', 'gamesWon', 'expWon', 'edge', 'created', 'updated']
    list_filter = ['user', 'type']
    
admin.site.register(Leaderboard, LeaderboardAdmin)
