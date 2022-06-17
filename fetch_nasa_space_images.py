import os
import requests

from random import randint
from dotenv import load_dotenv

from optimize_and_save_image import save_images_to_path, define_image_format


def nasa_space_img(nasa_token, counter, content_path):
    url_template = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': f'{nasa_token}',
        'count': f'{counter}'
    }
    response = requests.get(url_template,  params=params)
    response.raise_for_status()
    nasa_images_database = []
    for image in response.json():
        nasa_images_database.append(image['url'])
    defined_images = define_image_format(nasa_images_database)
    image_names, image_formats = (list(defined_images.keys()),
                                  list(defined_images.values()))
    save_images_to_path(nasa_images_database, content_path,
                        image_names, image_formats)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    content_path = 'images'
    counter = randint(1, 50)
    nasa_space_img(nasa_token, counter, content_path)
