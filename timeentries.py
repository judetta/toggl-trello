from togglapiutils import get_summary_report
from trelloapiutils import list_ids, getTrelloCards
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

print(time_entries)

# Get cards from trello
for list_id in list_ids.values():
    response = getTrelloCards(list_id)
    # Put cards in a dict with name as key and card id as value
    cards = {}
    for card in response:
        cards.update({card['name']: card['id']})
    print(cards)