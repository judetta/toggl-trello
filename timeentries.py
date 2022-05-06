from togglapiutils import get_summary_report, ms_to_hours
from trelloapiutils import TrelloIds, get_trello_cards, update_time_spent, get_current_time_spent


# Get summary report from Toggl and save projects and spent time in a dict
time_entries = {}
summary_report = get_summary_report()
try:    
    for item in summary_report['data']:
        time_entries.update({
            item['title']['project']: ms_to_hours(item['time'])})
except:
    print('Please check the request.')

# Get cards for active courses from Trello and put them in a dict 
# with name as key and card id as value
cards = {}
for list_id in TrelloIds.active_courses.values():
    response = get_trello_cards(list_id)
    for card in response:
        cards.update({card['name']: card['id']})

# Combine card ids and time entries into a single dict for update function
time_for_card = {}
for card_name, card_id in cards.items():
    if (card_name in time_entries.keys() 
        and time_entries[card_name] != get_current_time_spent(card_id)):
        time_for_card.update({card_id: time_entries[card_name]})

if len(time_for_card) == 0:
    print('There was nothing to update')
else:
    for card_id, time_spent in time_for_card.items():
        update_time_spent(card_id, time_spent)
