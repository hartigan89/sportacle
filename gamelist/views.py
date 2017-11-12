from .models import Sport, Game
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def GameList(request, sport_slug=None):
    sport = None
    sports = Sport.objects.all()
    games = Game.objects.all()
    if sport_slug:
        sport = get_object_or_404(Sport, slug=sport_slug)
        games = games.filter(sport=sport)
        
    return render(request, 'gamelist/gamelist.html', {'sport': sport, 'sports': sports, 'games': games})
