from togglapiutils import get_summary_report
import requests
from datetime import timedelta


# Get summary report from Toggl and save projects and spent time in a dict
time_entries = {}
summary_report = get_summary_report()
try:    
    for item in summary_report['data']:
        time_entries.update({
            item['title']['project']: str(timedelta(milliseconds=item['time']))})
except:
    print("Please check the request.")
