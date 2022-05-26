from importlib.resources import path
import os
import requests
from pathlib import Path


def load_images(image_url, image_path):
    filename = 'hubble.jpeg'
    Path(image_path).mkdir(parents=True, exist_ok=True)
    response = requests.get(image_url)
    response.raise_for_status()

    with open(os.path.join(image_path, filename), 'wb') as file:
        file.write(response.content)

if __name__ == '__main__':
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
    image_path = 'images'
    load_images(image_url, image_path)