time_spent_field_id = '603fc76549818d1e7bc152a3'
board_id: '5f05c61c34d07b2234c58ec9'


# Get Trello API key and token from files
with open('trello-api-key.txt') as f1, open('trello-api-token.txt') as f2:
    apikey = f1.read()
    apitoken = f2.read()



headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': 'github.com/judetta/toggl-trello'
}