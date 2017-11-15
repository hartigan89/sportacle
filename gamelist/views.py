from pytz import timezone
from datetime import datetime
from .models import Sport, Game
from django.shortcuts import render, redirect, get_object_or_404

def GameList(request, sport_slug=None):
    now = datetime.now(timezone('UTC'))

    sport = None
    sports = Sport.objects.all()
    games = Game.objects.filter(gameTime__gt=now)
    if sport_slug:
        sport = get_object_or_404(Sport, slug=sport_slug)
        games = games.filter(sport=sport)
        
    return render(request, 'gamelist/gamelist.html', {'sport': sport, 'sports': sports, 'games': games})
