import requests
from random import randint


def nasa_space_img(nasa_token):
    url_template = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': f'{nasa_token}',
        'count': f'{randint(1,50)}'
    }
    nasa_images_database = []
    response = requests.get(url_template,  params=params)
    response.raise_for_status()
    for i in response.json():
        nasa_images_database.append(i['url'])
    return nasa_images_database
