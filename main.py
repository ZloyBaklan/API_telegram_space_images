from importlib.resources import path
import os
import datetime
from random import randint
from urllib.parse import urlparse, unquote
import requests
from pathlib import Path
from dotenv import load_dotenv


def saving_images(content, content_path):
    Path(content_path).mkdir(parents=True, exist_ok=True)
    count = 0
    for i in content:
        filename = f'space_{count}.jpg'
        with open(os.path.join(content_path, filename), 'wb') as file:
            file.write(requests.get(i).content)
        count+=1

def fetch_spacex_last_launch(content_url):
    params = {}
    response = requests.get(content_url, params=params)
    response.raise_for_status()
    filtered_response = response.json()['links']['flickr']['original']
    spacex_images_database = []
    for i in filtered_response:
        spacex_images_database.append(i)
    return spacex_images_database

def nasa_space_img(nasa_token):
    url_template = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': f'{nasa_token}',
        'count':f'{randint(1,50)}'
    }
    nasa_images_database = []
    response = requests.get(url_template,  params=params)
    response.raise_for_status()
    for i in response.json():
        nasa_images_database.append(i['url'])
    return nasa_images_database

def define_image_format(test_url):
    image_name = os.path.split(urlparse(test_url).path)
    image_format = os.path.splitext(unquote(image_name[-1]))
    return image_format

def nasa_epic_images(nasa_token):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': f'{nasa_token}',
    }
    response = requests.get(epic_url,  params=params)
    image_datetime, image_name = response.json()[-1]['date'], response.json()[-1]['image']
    image_date = datetime.datetime.strptime(image_datetime, '%Y-%m-%d %H:%M:%S')
    main_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date.strftime("%Y/%m/%d")}/png/{image_name}.png'
    params_main = {
        'api_key': f'{nasa_token}',
    }
    response_main = requests.get(main_url,  params=params_main)
    print (response_main.url)

if __name__ == '__main__':
    flight_id = '5eb87d47ffd86e000604b38a'
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    content_path = 'images'
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    # nasa_space_img(nasa_token)
    # print(define_image_format(nasa_url))
    # fetch_spacex_last_launch(content_url)
    # saving_images(nasa_images, content_path)
    nasa_epic_images(nasa_token)