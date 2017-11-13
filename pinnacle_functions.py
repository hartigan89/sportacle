import requests
from requests.auth import HTTPBasicAuth
import json

def getSportID(base_url, username, password, sport):
    url = base_url + '/v2/sports'
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    sports = json.loads(req.text)

    for item in sports["sports"]:
        if item["name"] == sport:
            sportID = item["id"]

    return sportID

def getLeagueID(base_url, username, password, sportID, league):
    url = base_url + '/v2/leagues?sportId=' + str(sportID)
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    leagues = json.loads(req.text)

    for item in leagues["leagues"]:
        if item["name"] == league:
            leagueID = item["id"]

    return leagueID

def getFixtures(base_url, username, password, sportID, leagueID):
    url = base_url + '/v1/fixtures?sportId=' + str(sportID) + '&leagueIds=' + str(leagueID)
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    fixtures = json.loads(req.text)
    return fixtures

def getOdds(base_url, username, password, sportID, leagueID):
    url = base_url + '/v1/odds?sportId=' + str(sportID) + '&leagueIds=' + str(leagueID)
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    odds = json.loads(req.text)
    return odds

def getLine(base_url, username, password, sportID, leagueID, eventID, team):
    url = base_url + '/v1/line?sportId=' + str(sportID) + '&leagueId=' + str(leagueID) + '&eventID=' + str(eventID) + '&team=' + team + '&betType=MONEYLINE&oddsFormat=DECIMAL&periodNumber=0'
    req = requests.get(url, auth=HTTPBasicAuth(username, password))
    line = json.loads(req.text)
    return line

