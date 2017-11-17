from __future__ import absolute_import, unicode_literals
from celery import shared_task
from pytz import timezone
from datetime import datetime
from django.contrib.auth.models import User
from pinnacle_functions import getOdds, getSportID, getLeagueID, getFixtures, getLine, getResults
from gamelist.models import Sport, League, Game
from leaderboard.models import Leaderboard
from ranker.ranker import getRank
from ranker.models import Rank

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

@shared_task()
def update_ranks():
    users = User.objects.all()
    for u in users:
        tempRank = Rank.objects.filter(user=u).order_by('-updated')
        if tempRank:
            currSmoothRank = float(tempRank[0].smoothRank)
            lastUpdate = int(tempRank[0].numGames)
        else:
            currSmoothRank = 0

        stats = Leaderboard.objects.filter(user=u, type="A")[0]
        numGames = stats.numGames
        pValue = stats.pValue

        if numGames != lastUpdate:
            dict = getRank(numGames, pValue, currSmoothRank)

            trueRank = dict["trueRank"]
            smoothRank = dict["smoothRank"]
            rank = dict["rank"]

            Rank.objects.create(user=u,
                                numGames=numGames,
                                trueRank=trueRank,
                                smoothRank=smoothRank,
                                rank=rank,
                                )

@shared_task()
def update_leaderboard():
    # clear leaderboard
    Leaderboard.objects.all().delete()

    today = datetime.date.today()
    weekDate = today - datetime.timedelta(days=7)
    monthDate = today - datetime.timedelta(days=30)

    users = User.objects.all()
    for u in users:
        lastWeek = Pick.objects.filter(user=u, updated__range=[weekDate, today])
        lastMonth = Pick.objects.filter(user=u, updated__range=[monthDate, today])
        allTime = Pick.objects.filter(user=u)

        # weekly leaderboard
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

        # monthly leaderboard
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

        # all-time leaderboard
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
