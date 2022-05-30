from importlib.resources import path
import os
import requests
from pathlib import Path


def fetch_spacex_last_launch(content_url, content_path):
    Path(content_path).mkdir(parents=True, exist_ok=True)
    response = requests.get(content_url)
    response.raise_for_status()
    count = 0
    for i in response.json()['links']['flickr']['original']:
        filename = f'space_{count}.jpg'
        count +=1
        with open(os.path.join(content_path, filename), 'wb') as file:
            file.write(requests.get(i).content)

if __name__ == '__main__':
    flight_id = '5eb87d47ffd86e000604b38a'
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    content_path = 'images'
    fetch_spacex_last_launch(content_url, content_path)