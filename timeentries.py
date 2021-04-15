from togglapiutils import get_summary_report, ms_to_hours
from trelloapiutils import list_ids, get_trello_cards, update_time_spent


# Get summary report from Toggl and save projects and spent time in a dict
time_entries = {}
summary_report = get_summary_report()
try:    
    for item in summary_report['data']:
        time_entries.update({
            item['title']['project']: ms_to_hours(item['time'])})
except:
    print('Please check the request.')

#print(time_entries)

# Get cards from trello
#for list_id in list_ids.values():
list_id = list_ids.get('waiting_for_credits_list_id')
response = get_trello_cards(list_id)
# Put cards in a dict with name as key and card id as value
cards = {}
for card in response:
    cards.update({card['name']: card['id']})

#print(cards)

"""
result = {}
for key in cards.keys():
    result[cards[key]] = time_entries[key]
"""

time_with_card_id = {cards[key]: time_entries[key] for key in cards.keys()}

for card_id, time_spent in time_with_card_id.items():
    update_time_spent(card_id, time_spent)

print(time_with_card_id)