import requests

# Possibly needed id's from Trello
class TrelloIds:
    active_courses = {
    'courses_in_progress_list': '5f05c6d175bfc506e1166f54', 
    'waiting_for_credits_list': '5f3fbe38e514972615f51799'
    }

    finished_courses_list = '5f05c6d5ba81e62525d73f35'

    # idCustomField, same for all cards
    time_spent_field = '603fc76549818d1e7bc152a3' 


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
    """Returns all cards in a specific list on Trello by list id, in json format"""
    url = 'https://api.trello.com/1/lists/' + list_id + '/cards'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Cannot get Trello cards, error', response.status_code)
    else:
        return response.json()


def get_card_name(card_id):
    """Returns Trello card name by card id"""
    url = 'https://api.trello.com/1/cards/' + card_id + '/?fields=name'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Cannot get Trello card name, error', response.status_code)
    else:
        response = response.json()
        return response['name']


def update_time_spent(card_id, time_spent):
    """Updates 'Time spent' custom field on a specified Trello card
    
    Arguments:
    card_id: Trello card id, string
    time_spent: Value to be entered into 'Time spent' field, string
    """
    url = ('https://api.trello.com/1/card/' + card_id 
            + '/customField/' + TrelloIds.time_spent_field + '/item')
    response = requests.put(url, headers=headers, params=params, 
            json={'value': {'text': time_spent}})
    if response.status_code == 200:
        print(get_card_name(card_id) + ' successfully updated')
    else:
        print('Update failed for ' + get_card_name(card_id))


def get_current_time_spent(card_id):
    """Returns the current value in time spent field by card id"""
    url = 'https://api.trello.com/1/cards/' + card_id + '/?fields=name&customFieldItems=true'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print('Error', response.status_code, 'getting custom fields')
    else:
        data = response.json()
        for item in data['customFieldItems']:
            if item['idCustomField'] == TrelloIds.time_spent_field:
                return item['value']['text']
