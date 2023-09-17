import requests
import json
from fuzzywuzzy import fuzz


def get_free_games():
    api_key = '99b377b598c64bedb6340c8d535e7516'

    # Define the base URL for the RAWG API
    base_url = 'https://api.rawg.io/api/games'

    # Construct the full URL for the API call to get free games
    url = f'{base_url}?key={api_key}&filters=free'

    # Make the API call
    response = requests.get(url)

    return response



    


def get_game_info(game_name):
    api_key = '99b377b598c64bedb6340c8d535e7516'

    base_url = 'https://api.rawg.io/api/games'

    # Construct the full URL for the API call to get free games
    url = f'{base_url}?key={api_key}&search={game_name}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        best_match = max(data['results'], key=lambda x: fuzz.token_sort_ratio(x['name'], game_name))

        return{
            'name': best_match['name'],
            'platforms':[platform['platform']['name'] for platform in best_match['platforms']]
        }
    else:
        return None
    


def get_discounted_games():
    api_key = '99b377b598c64bedb6340c8d535e7516'

    base_url = 'https://api.rawg.io/api/games'

    params = {'key': api_key, 'discounted': 'true'}

    response = requests.get(base_url, params = params)

    if response.status_code == 200:
        return response.json()
    else:
        return None



    

        

        

def main():




    gameInfo = get_discounted_games()

    if gameInfo:
        for game in gameInfo['results']:
            print(game["name"])
        



    # response = get_free_games()

    # # Check if the request was successful (status code 200)
    # if response.status_code == 200:
    #     # Parse the JSON response
    #     data = response.json()
    #     for game in data['results']:
    #         print(game["name"])
    # else:
    #     # If the request was unsuccessful, print an error message
    #     print(f'Error: {response.status_code}')


if __name__ == "__main__":
    main()
