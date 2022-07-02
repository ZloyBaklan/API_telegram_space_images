import os
import requests

from random import randint
from dotenv import load_dotenv

from optimize_and_save_image import save_images_to_path, define_image_format


def get_nasa_space_img(nasa_token, content_response_count, content_path):
    url_template = 'https://api.nasa.gov/planetary/apod'
    request_params = {
        'api_key': nasa_token,
        'count': f'{content_response_count}'
    }
    response = requests.get(url_template,  params=request_params)
    response.raise_for_status()
    nasa_images_list = []
    for image in response.json():
        nasa_images_list.append(image['url'])
    for link in nasa_images_list:
        defined_image_name, defined_image_format = define_image_format(link)
        save_images_to_path(
            link,
            content_path,
            defined_image_format,
            defined_image_name
            )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    content_path = 'images'
    content_response_count = 25
    get_nasa_space_img(nasa_token, content_response_count, content_path)
