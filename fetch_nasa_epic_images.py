import argparse
import os
import requests

from dotenv import load_dotenv
from datetime import datetime

from optimize_and_save_image import save_images_to_path, define_image_format


def get_nasa_epic_images(nasa_token, content_response_count, content_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    request_params = {
        'api_key': nasa_token,
    }
    response = requests.get(epic_url,  params=request_params)
    response.raise_for_status()
    nasa_epic_images_list = []
    content_response = response.json()[:content_response_count]
    for image_content in content_response:
        image_datetime, image_name = (
            image_content['date'],
            image_content['image']
            )
        img_date = datetime.fromisoformat(image_datetime).strftime('%Y/%m/%d')
        image_url = ('https://api.nasa.gov/EPIC/archive/natural/'
                    f'{img_date}/png/{image_name}.png')
        request_params_image_url = {
            'api_key': nasa_token,
        }
        response_main = requests.get(
            image_url,
            params=request_params_image_url
            )
        response_main.raise_for_status()
        nasa_epic_images_list.append(response_main.url)
    for link in nasa_epic_images_list:
        defined_name, defined_format = define_image_format(link)
        save_images_to_path(
            link,
            content_path,
            defined_format,
            defined_name
            )


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    parser = argparse.ArgumentParser(description='Argeuments for script.')
    parser.add_argument(
        'content_response_count',
        type=int,
        help='Count of content response.'
        )
    parser.add_argument(
        'content_path',
        type=str,
        help='Name of the content path.'
        )
    args = parser.parse_args()
    get_nasa_epic_images(
        nasa_token,
        args.content_response_count,
        args.content_path
        )
