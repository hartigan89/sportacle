from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pytz import timezone
from datetime import datetime
from pinnacle_functions import getOdds, getSportID, getLeagueID, getFixtures, getLine, getResults
from gamelist.models import Sport, League, Game
from leaderboard.tasks import update_leaderboard

@shared_task()
def update_odds():
    base_url = "https://api.pinnaclesports.com"
    username = "KH998812"
    password = "Stewart11!"

    # get nfl games
    sport = Sport.objects.filter(name="Football")[0]
    league = League.objects.filter(name="NFL")[0]

    sportID = getSportID(base_url, username, password, "Football")
    leagueID = getLeagueID(base_url, username, password, sportID, "NFL")

    odds = getOdds(base_url, username, password, sportID, leagueID)
    fixtures = getFixtures(base_url, username, password, sportID, leagueID)

    for game in odds["leagues"][0]["events"]:
        # get event info
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
                Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,
                                                                                    homeOdds=homeLine)
            else:
                Game.objects.create(pinnacleID=str(eventID), sport=sport, league=league, gameTime=gameTime,
                                    visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine, outcome='U')

    # get nhl games
    sport = Sport.objects.filter(name="Hockey")[0]
    league = League.objects.filter(name="NHL")[0]

    sportID = getSportID(base_url, username, password, "Hockey")
    leagueID = getLeagueID(base_url, username, password, sportID, "NHL OT Included")

    odds = getOdds(base_url, username, password, sportID, leagueID)
    fixtures = getFixtures(base_url, username, password, sportID, leagueID)

    for game in odds["leagues"][0]["events"]:
        # get event info
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

            if not visitor == "Away Goals":
                if Game.objects.filter(visitor=visitor, home=home, outcome='U'):
                    Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,
                                                                                        homeOdds=homeLine)
                else:
                    Game.objects.create(pinnacleID=str(eventID), sport=sport, league=league, gameTime=gameTime,
                                        visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine,
                                        outcome='U')

    # get nba games
    sport = Sport.objects.filter(name="Basketball")[0]
    league = League.objects.filter(name="NBA")[0]

    sportID = getSportID(base_url, username, password, "Basketball")
    leagueID = getLeagueID(base_url, username, password, sportID, "NBA")

    odds = getOdds(base_url, username, password, sportID, leagueID)
    fixtures = getFixtures(base_url, username, password, sportID, leagueID)

    for game in odds["leagues"][0]["events"]:
        # get event info
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
                Game.objects.filter(visitor=visitor, home=home, outcome='U').update(visitorOdds=visitorLine,
                                                                                    homeOdds=homeLine)
            else:
                Game.objects.create(pinnacleID=str(eventID), sport=sport, league=league, gameTime=gameTime,
                                    visitor=visitor, visitorOdds=visitorLine, home=home, homeOdds=homeLine, outcome='U')

@shared_task()
def update_results():
    base_url = "https://api.pinnaclesports.com"
    username = "KH998812"
    password = "Stewart11!"

    # update NFL scores
    sport = Sport.objects.filter(name="Football")[0]
    league = League.objects.filter(name="NFL")[0]

    sportID = getSportID(base_url, username, password, "Football")
    leagueID = getLeagueID(base_url, username, password, sportID, "NFL")

    games = Game.objects.filter(sport=sport, league=league, outcome="U")
    results = getResults(base_url, username, password, sportID, leagueID)

    for game in games:
        pinnacleID = game.pinnacleID

        for event in results["leagues"][0]["events"]:
            if pinnacleID == str(event["id"]):
                periods = event["periods"]
                for period in periods:
                    if period["number"]==0:
                        awayScore = period["team1Score"]
                        homeScore = period["team2Score"]

                        if awayScore > homeScore:
                            outcome = "V"
                        elif homeScore > awayScore:
                            outcome = "H"
                        else:
                            outcome = "T"

                        game.outcome = outcome
                        game.save(update_fields=['outcome'])

    # update NHL scores
    sport = Sport.objects.filter(name="Hockey")[0]
    league = League.objects.filter(name="NHL")[0]

    sportID = getSportID(base_url, username, password, "Hockey")
    leagueID = getLeagueID(base_url, username, password, sportID, "NHL OT Included")

    games = Game.objects.filter(sport=sport, league=league, outcome="U")
    results = getResults(base_url, username, password, sportID, leagueID)

    for game in games:
        pinnacleID = game.pinnacleID

        for event in results["leagues"][0]["events"]:
            if pinnacleID == str(event["id"]):
                periods = event["periods"]
                for period in periods:
                    if period["number"] == 0:
                        awayScore = period["team1Score"]
                        homeScore = period["team2Score"]

                        if awayScore > homeScore:
                            outcome = "V"
                        elif homeScore > awayScore:
                            outcome = "H"
                        else:
                            outcome = "T"

                        game.outcome = outcome
                        game.save(update_fields=['outcome'])

    # update NBA scores
    sport = Sport.objects.filter(name="Basketball")[0]
    league = League.objects.filter(name="NBA")[0]

    sportID = getSportID(base_url, username, password, "Basketball")
    leagueID = getLeagueID(base_url, username, password, sportID, "NBA")

    games = Game.objects.filter(sport=sport, league=league, outcome="U")
    results = getResults(base_url, username, password, sportID, leagueID)

    for game in games:
        pinnacleID = game.pinnacleID

        for event in results["leagues"][0]["events"]:
            if pinnacleID == str(event["id"]):
                periods = event["periods"]
                for period in periods:
                    if period["number"] == 0:
                        awayScore = period["team1Score"]
                        homeScore = period["team2Score"]

                        if awayScore > homeScore:
                            outcome = "V"
                        elif homeScore > awayScore:
                            outcome = "H"
                        else:
                            outcome = "T"

                        game.outcome = outcome
                        game.save(update_fields=['outcome'])

    #call next task
    update_leaderboard.delay()