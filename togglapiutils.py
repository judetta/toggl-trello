from base64 import b64encode
from datetime import date, timedelta


# Toggl reports API allows to fetch data only for one year's period,
# thus get the date one year before today
year_ago = str(date.today() - timedelta(days=365))

# Craft the authentication string for Toggl
with open('toggl-api-token.txt') as f:
    apitoken = f.read()
authheader = apitoken + ':' + 'api_token'
authheader = 'Basic ' + b64encode(
    authheader.encode()).decode('ascii').rstrip()

# Details for requests towards Toggl APIs
project_data_url = 'https://api.track.toggl.com/api/v8/workspaces/4998714/projects'
summary_report_url = 'https://toggl.com/reports/api/v2/summary'
headers = {
    'Authorization': authheader,
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': 'github.com/judetta/toggl-trello'
}
parameters = {                # Params for reports API
    'user_agent': 'github.com/judetta/toggl-trello',
    'workspace_id': '4998714',
    'since':  year_ago
}

