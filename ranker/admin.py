from django.contrib import admin
from .models import Rank

class RankAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'numGames', 'trueRank', 'smoothRank', 'rank', 'created', 'updated']
    list_filter = ['user', 'created', 'updated']
    
admin.site.register(Rank, RankAdmin)
