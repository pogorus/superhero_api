import requests

API_BASE_URL = 'https://superheroapi.com/api/2619421814940190/'

def get_smartest_superhero(*superheros):
    max_superhero_int = 0
    smartest_superhero = ''
    for superhero in superheros:
        superhero_int = requests.get(API_BASE_URL + 'search/' + superhero).json()['results'][0]['powerstats']['intelligence']
        if int(superhero_int) > int(max_superhero_int):
            max_superhero_int = superhero_int
            smartest_superhero = superhero

    return print(f'Самый умный супергерой {smartest_superhero}, его интелект - {max_superhero_int}')

get_smartest_superhero('Hulk', 'Thanos', 'Captain America')