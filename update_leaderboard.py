import os
import sys
import django
sys.path.append("/home/ubuntu/workspace/") #path to your settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'sportacle.settings.dev'
django.setup()

import datetime
from decimal import Decimal
from picks.models import Pick
from leaderboard.stats import getStats
from django.contrib.auth.models import User
from gamelist.models import Game
from ranker.models import Rank
from leaderboard.models import Leaderboard

#clear leaderboard
Leaderboard.objects.all().delete()

today = datetime.date.today()
weekDate = today - datetime.timedelta(days=7)
monthDate = today - datetime.timedelta(days=30)
    
users = User.objects.all()
for u in users:
    lastWeek = Pick.objects.filter(user=u, updated__range=[weekDate, today])
    lastMonth = Pick.objects.filter(user=u, updated__range=[monthDate, today])
    allTime = Pick.objects.filter(user=u)
    
    #weekly leaderboard
    prob = []
    gamesWon = 0
    for p in lastWeek:
        outcome = Game.objects.filter(id=p.game.id)[0].outcome
        if outcome != 'U' and outcome != 'T':
            prob.append(float(p.probability))
            selection = p.selection
            
            if outcome == selection:
                gamesWon = gamesWon + 1
    
    dict = getStats(prob, gamesWon)
    
    numGames = dict["numGames"]
    expWon = dict["expWon"]
    edge = dict["edge"]
    p = dict["p"]
    
    type = "W"
    Leaderboard.objects.create(user=u,
                            type=type,
                            numGames=numGames,
                            gamesWon=gamesWon,
                            expWon=expWon,
                            edge=edge,
                            pValue=p,
                            )
    
   #monthly leaderboard
    prob = []
    gamesWon = 0
    for p in lastMonth:
        outcome = Game.objects.filter(id=p.game.id)[0].outcome
        if outcome != 'U' and outcome != 'T':
            prob.append(float(p.probability))
            selection = p.selection
            
            if outcome == selection:
                gamesWon = gamesWon + 1
    
    dict = getStats(prob, gamesWon)
    
    numGames = dict["numGames"]
    expWon = dict["expWon"]
    edge = dict["edge"]
    p = dict["p"]
    
    type = "M"
    Leaderboard.objects.create(user=u,
                            type=type,
                            numGames=numGames,
                            gamesWon=gamesWon,
                            expWon=expWon,
                            edge=edge,
                            pValue=p,
                            )
    
    #all-time leaderboard
    prob = []
    gamesWon = 0
    for p in allTime:
        outcome = Game.objects.filter(id=p.game.id)[0].outcome
        if outcome != 'U' and outcome != 'T':
            prob.append(float(p.probability))
            selection = p.selection
            
            if outcome == selection:
                gamesWon = gamesWon + 1
    
    dict = getStats(prob, gamesWon)
    
    numGames = dict["numGames"]
    expWon = dict["expWon"]
    edge = dict["edge"]
    p = dict["p"]
    
    type = "A"
    Leaderboard.objects.create(user=u,
                            type=type,
                            numGames=numGames,
                            gamesWon=gamesWon,
                            expWon=expWon,
                            edge=edge,
                            pValue=p,
                            )
    