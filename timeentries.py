import requests
from base64 import b64encode


def ms_to_hours(milliseconds):
    '''Convert milliseconds into format hh:mm:ss'''
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


user_agent = 'github.com/judetta/toggl-trello'

# craft the authentication string for toggl
with open('toggl-api-token.txt') as f:
    apitoken = f.read()
authheader = apitoken + ':' + 'api_token'
authheader = 'Basic ' + b64encode(authheader.encode()).decode('ascii').rstrip()

# details for requests towards toggl
project_data_url = 'https://api.track.toggl.com/api/v8/workspaces/4998714/projects'
summary_report_url = 'https://toggl.com/reports/api/v2/summary'
headers = {
    'Authorization': authheader,
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': user_agent
}
parameters = {
    'user_agent': user_agent,
    'workspace_id': '4998714',
    'since':  '2021-01-01'
}


# get summary report and print out projects and time spent on each
summary_report = requests.get(summary_report_url, headers=headers, params=parameters).json()
for item in summary_report['data']:
    print(item['title']['project'], ms_to_hours(item['time']))




'''
response = requests.get(project_data_url, headers=headers).json()

project_ids = []
for project in response:
    project_id = project['id']
    project_ids.append(project_id)

print(project_ids)
'''