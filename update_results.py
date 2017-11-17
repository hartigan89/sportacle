import os
import sys
import django
sys.path.append("/home/ubuntu/workspace/") #path to your settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'sportacle.settings'
django.setup()

from pinnacle_functions import getOdds, getSportID, getLeagueID, getFixtures, getLine, getResults
from gamelist.models import Sport, League, Game

base_url = "https://api.pinnaclesports.com"
username = "KH998812"
password = "Stewart11!"

#update NFL scores
sport = Sport.objects.filter(name="Football")[0]
league = League.objects.filter(name="NFL")[0]

sportID = getSportID(base_url, username, password, "Football")
leagueID = getLeagueID(base_url, username, password, sportID, "NFL")

games = Game.objects.filter(sport=sport, league=league, outcome="U")
results = getResults(base_url, username, password, sportID, leagueID)

for game in games:
    pinnacleID=game.pinnacleID

    for event in results["leagues"][0]["events"]:
        if pinnacleID==str(event["id"]):
            awayScore = event["periods"][0]["team1Score"]
            homeScore = event["periods"][0]["team2Score"]

            if awayScore > homeScore:
                outcome = "V"
            elif homeScore > awayScore:
                outcome = "H"
            else:
                outcome = "T"

            game.outcome = outcome
            game.save(update_fields=['outcome'])

#update NHL scores
sport = Sport.objects.filter(name="Hockey")[0]
league = League.objects.filter(name="NHL")[0]

sportID = getSportID(base_url, username, password, "Hockey")
leagueID = getLeagueID(base_url, username, password, sportID, "NHL OT Included")

games = Game.objects.filter(sport=sport, league=league, outcome="U")
results = getResults(base_url, username, password, sportID, leagueID)

for game in games:
    pinnacleID=game.pinnacleID

    for event in results["leagues"][0]["events"]:
        if pinnacleID==str(event["id"]):
            awayScore = event["periods"][0]["team1Score"]
            homeScore = event["periods"][0]["team2Score"]

            if awayScore > homeScore:
                outcome = "V"
            elif homeScore > awayScore:
                outcome = "H"
            else:
                outcome = "T"

            game.outcome = outcome
            game.save(update_fields=['outcome'])

#update NBA scores
sport = Sport.objects.filter(name="Basketball")[0]
league = League.objects.filter(name="NBA")[0]

sportID = getSportID(base_url, username, password, "Basketball")
leagueID = getLeagueID(base_url, username, password, sportID, "NBA")

games = Game.objects.filter(sport=sport, league=league, outcome="U")
results = getResults(base_url, username, password, sportID, leagueID)

for game in games:
    pinnacleID=game.pinnacleID

    for event in results["leagues"][0]["events"]:
        if pinnacleID==str(event["id"]):
            awayScore = event["periods"][0]["team1Score"]
            homeScore = event["periods"][0]["team2Score"]

            if awayScore > homeScore:
                outcome = "V"
            elif homeScore > awayScore:
                outcome = "H"
            else:
                outcome = "T"

            game.outcome = outcome
            game.save(update_fields=['outcome'])