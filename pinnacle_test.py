import requests
from requests.auth import HTTPBasicAuth
import base64
import uuid
import json

base_url = "https://api.pinnaclesports.com"
username = "KH998812"
password = "Stewart11!"

url = base_url + "/v1/client/balance"

req = requests.get(url, auth=HTTPBasicAuth(username, password))
print(req.status_code)
print(req.text)