from base64 import b64encode
from datetime import date, timedelta
import requests

# Toggl reports API allows to fetch data only for one year's period,
# thus get the date one year before today
year_ago = str(date.today() - timedelta(days=365))

# Craft the authentication string for Toggl
with open('toggl-api-token.txt') as f:
    apitoken = f.read()
authheader = apitoken + ':' + 'api_token'
authheader = 'Basic ' + b64encode(
    authheader.encode()).decode('ascii').rstrip()

# Define the headers used for all requests
headers = {
    'Authorization': authheader,
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': 'github.com/judetta/toggl-trello'
}


# this might be needed later:
# project_data_url = 'https://api.track.toggl.com/api/v8/workspaces/4998714/projects'


def get_summary_report():
    """Returns the summary report from Toggl Track in json format."""
    url = 'https://api.track.toggl.com/reports/api/v2/summary'
    params = {
        'user_agent': 'github.com/judetta/toggl-trello',
        'workspace_id': '4998714',
        'since':  year_ago
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Toggl report summary request not successful, error code', response.status_code)
    else:
        return response.json()


# Function to format output from Toggl
def ms_to_hours(milliseconds):
    """Convert milliseconds into format (h)h:mm:ss"""
    seconds = milliseconds / 1000
    minutes = seconds // 60
    seconds -= minutes * 60
    hours = minutes // 60
    minutes -= hours * 60
    if minutes < 10:
        minutes = '0' + str(int(minutes))
    else:
        minutes = str(int(minutes))
    if seconds < 10:
        seconds = '0' + str(int(seconds))
    else:
        seconds = str(int(seconds))
    return f'{int(hours)}:{minutes}:{seconds}'