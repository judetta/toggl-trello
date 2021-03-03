from togglapiutils import (
    summary_report_url, 
    headers as toggl_heads, 
    parameters as toggl_params)
import requests
from datetime import timedelta


# Get summary report from Toggl and save projects and spent time in a dict
time_entries = {}
summary_report = requests.get(
    summary_report_url, 
    headers=toggl_heads, 
    params=toggl_params).json()
for item in summary_report['data']:
    time_entries.update({
        item['title']['project']: str(timedelta(milliseconds=item['time']))})

print(time_entries)
