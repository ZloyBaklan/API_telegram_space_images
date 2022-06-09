import os
import requests

from random import randint
from dotenv import load_dotenv

def nasa_space_img(nasa_token, counter):
    url_template = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': f'{nasa_token}',
        'count': f'{counter}'
    }
    response = requests.get(url_template,  params=params)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    nasa_images_database = []
    counter = randint(1,50)
    for image in nasa_space_img(nasa_token, counter):
        nasa_images_database.append(image['url'])
