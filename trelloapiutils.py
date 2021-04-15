import requests

# Possibly needed id's from Trello
list_ids = {
'courses_in_progress_list_id': '5f05c6d175bfc506e1166f54', 
'waiting_for_credits_list_id': '5f3fbe38e514972615f51799'
}
#'finished_courses_list_id': '5f05c6d5ba81e62525d73f35'

# idCustomField, same for all cards
time_spent_field_id = '603fc76549818d1e7bc152a3' 

# Get Trello API key and token from files
with open('trello-api-key.txt') as f1, open('trello-api-token.txt') as f2:
    apikey = f1.read()
    apitoken = f2.read()

# Headers and parameters used for all requests
headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': 'github.com/judetta/toggl-trello'
}

params = {
    'key': apikey,
    'token': apitoken
}


def get_trello_cards(list_id):
    """Get all cards in a specific list on Trello by list id"""
    url = 'https://api.trello.com/1/lists/' + list_id + '/cards'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Error' + response.status_code)
    else:
        return response.json()


def get_card_name(card_id):
    """Get Trello card name by card id"""
    url = 'https://api.trello.com/1/cards/' + card_id + '/?fields=name'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Error' + response.status_code)
    else:
        response = response.json()
        return response['name']


def update_time_spent(card_id, time_spent):
    url = ('https://api.trello.com/1/card/' 
        + card_id + '/customField/' 
        + time_spent_field_id + '/item')
    response = requests.put(url, headers=headers, params=params, 
        json={'value': {'text': time_spent}})
    if response.status_code == 200:
        print(get_card_name(card_id) + ' successfully updated')
    else:
        print('Update failed for ' + get_card_name(card_id))

