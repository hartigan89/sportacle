import requests
from requests.auth import HTTPBasicAuth
import json
from pinnacle_functions import getOdds, getSportID, getLeagueID

base_url = "https://api.pinnaclesports.com"
username = "KH998812"
password = "Stewart11!"

sportID = getSportID(base_url, username, password, "Basketball")
leagueID = getLeagueID(base_url, username, password, sportID, "NBA")

url = base_url + '/v2/leagues?sportId=' + str(sportID)
#url = base_url + '/v2/sports'
#url = base_url + '/v1/fixtures?sportId=' + str(sportID) + '&leagueIDs=' + str(leagueID)
#url = base_url + '/v1/fixtures/settled?sportId=' + str(sportID) + '&leagueIDs=' + str(leagueID)
#url = base_url + '/v1/line?sportId=' + str(sportID) + '&leagueID=' + str(leagueID) + '&eventID=784380443&betType=MONEYLINE&team=Team1&oddsFormat=DECIMAL&periodNumber=0'
#url = base_url + '/v1/odds?sportId=' + str(sportID) + '&leagueIDs=' + str(leagueID)

req = requests.get(url, auth=HTTPBasicAuth(username, password))
print(req.status_code)
print(req.text)
