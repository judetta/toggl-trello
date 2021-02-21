import json
import requests
from base64 import b64encode

# craft the authentication string 
with open('toggl-api-token.txt') as f:
    apitoken = f.read()
authHeader = apitoken + ":" + "api_token"
authHeader = "Basic " + b64encode(authHeader.encode()).decode('ascii').rstrip()


url = 'https://api.track.toggl.com/api/v8/workspaces/4998714/projects'
headers = {
        "Authorization": authHeader,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": "python/urllib",
    }

response = requests.get(url, headers=headers).json()

for project in response:
    print(project['name'])