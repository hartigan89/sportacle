from django.contrib import admin
from .models import Sport, Game

# Register your models here.
class SportAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Sport, SportAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'sport', 'gameTime', 'visitor', 'visitorOdds', 'home', 'homeOdds', 'outcome', 'created', 'updated']
    list_filter = ['created', 'updated', 'sport']
    list_editable = ['visitorOdds', 'homeOdds','outcome']
admin.site.register(Game, GameAdmin)