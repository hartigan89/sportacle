import os
import sys
import django
sys.path.append("/home/ubuntu/workspace/") #path to your settings file
os.environ['DJANGO_SETTINGS_MODULE'] = 'sportacle.settings'
django.setup()

from pytz import timezone
from datetime import datetime
from datetime import timedelta
from pinnacle_functions import getOdds, getSportID, getLeagueID, getFixtures, getLine
from gamelist.models import Sport, League, Game

base_url = "https://api.pinnaclesports.com"
username = "KH998812"
password = "Stewart11!"

#get nfl games
sport = Sport.objects.filter(name="Football")[0]
league = League.objects.filter(name="NFL")[0]

sportID = getSportID(base_url, username, password, "Football")
leagueID = getLeagueID(base_url, username, password, sportID, "NFL")

odds = getOdds(base_url, username, password, sportID, leagueID)
fixtures = getFixtures(base_url, username, password, sportID, leagueID)

for game in odds["leagues"][0]["events"]:
    #get event info
    eventID = game["id"]

    status = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["status"]
    if status == "SUCCESS":
        visitorLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["price"]
        homeLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team2")["price"]

        for event in fixtures["league"][0]["events"]:
            if event["id"] == eventID:
                gameTime = datetime.strptime(event["starts"], "%Y-%m-%dT%H:%M:%SZ")
                gameTime = gameTime.replace(tzinfo=timezone('UTC'))
                visitor = event["away"]
                home = event["home"]

        if Game.objects.filter(visitor=visitor, home=home, outcome='U'):
            Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,homeOdds=homeLine)
        else:
            Game.objects.create(pinnacleID=str(eventID),sport=sport,league=league, gameTime=gameTime, visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine, outcome='U')

#get nhl games
sport = Sport.objects.filter(name="Hockey")[0]
league = League.objects.filter(name="NHL")[0]

sportID = getSportID(base_url, username, password, "Hockey")
leagueID = getLeagueID(base_url, username, password, sportID, "NHL OT Included")

odds = getOdds(base_url, username, password, sportID, leagueID)
fixtures = getFixtures(base_url, username, password, sportID, leagueID)

for game in odds["leagues"][0]["events"]:
    #get event info
    eventID = game["id"]

    status = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["status"]
    if status == "SUCCESS":
        visitorLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["price"]
        homeLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team2")["price"]

        for event in fixtures["league"][0]["events"]:
            if event["id"] == eventID:
                gameTime = datetime.strptime(event["starts"], "%Y-%m-%dT%H:%M:%SZ")
                gameTime = gameTime.replace(tzinfo=timezone('UTC'))
                visitor = event["away"]
                home = event["home"]

        if Game.objects.filter(visitor=visitor, home=home, outcome='U'):
            Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,homeOdds=homeLine)
        else:
            Game.objects.create(pinnacleID=str(eventID),sport=sport,league=league, gameTime=gameTime, visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine, outcome='U')

#get nba games
sport = Sport.objects.filter(name="Basketball")[0]
league = League.objects.filter(name="NBA")[0]

sportID = getSportID(base_url, username, password, "Basketball")
leagueID = getLeagueID(base_url, username, password, sportID, "NBA")

odds = getOdds(base_url, username, password, sportID, leagueID)
fixtures = getFixtures(base_url, username, password, sportID, leagueID)

for game in odds["leagues"][0]["events"]:
    #get event info
    eventID = game["id"]

    status = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["status"]
    if status == "SUCCESS":
        visitorLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team1")["price"]
        homeLine = getLine(base_url, username, password, sportID, leagueID, eventID, "Team2")["price"]

        for event in fixtures["league"][0]["events"]:
            if event["id"] == eventID:
                gameTime = datetime.strptime(event["starts"], "%Y-%m-%dT%H:%M:%SZ")
                gameTime = gameTime.replace(tzinfo=timezone('UTC'))
                visitor = event["away"]
                home = event["home"]

        if Game.objects.filter(visitor=visitor, home=home, outcome='U'):
            Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,homeOdds=homeLine)
        else:
            Game.objects.create(pinnacleID=str(eventID),sport=sport,league=league, gameTime=gameTime, visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine, outcome='U')