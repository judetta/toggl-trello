import requests


# Possibly needed id's from Trello
time_spent_field_id = '603fc76549818d1e7bc152a3'
board_id = '5f05c61c34d07b2234c58ec9'
courses_in_progress_list_id = '5f05c6d175bfc506e1166f54'
waiting_for_credits_list_id = '5f3fbe38e514972615f51799'
finished_courses_list_id = '5f05c6d5ba81e62525d73f35'

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


def getTrelloCards(list_id):
    """Get all the cards on Trello board"""
    url = 'https://api.trello.com/1/lists/' + list_id + '/cards'
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Error" + response.status_code)
    else:
        return response.json()

cards = {}
response = getTrelloCards(waiting_for_credits_list_id)
for card in response:
    cards.update({card['name']: card['id']})
print(cards)