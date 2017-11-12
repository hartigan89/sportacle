import requests  
import json
import datetime
import sys

"""
call the API
"""

url = "https://api.the-odds-api.com/v2/odds/?sport=UPCOMING&region=uk&apiKey=76000b6bea3fc896f75e191974275db6"
headers = {'content-type': 'application/json'}

req = requests.get(url, headers).text
json_data = json.loads(req)

print (json_data["data"][0])


