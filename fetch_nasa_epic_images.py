import argparse
import os
import requests

from dotenv import load_dotenv
from datetime import datetime

from optimize_and_save_image import save_images_to_path, define_image_format


def get_and_save_nasa_epic_images(nasa_token, response_content_count, content_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    request_params = {
        'api_key': nasa_token,
    }
    response_nasa_epic = requests.get(epic_url,  params=request_params)
    response_nasa_epic.raise_for_status()
    nasa_epic_images = []
    response_content = response_nasa_epic.json()[:response_content_count]
    for image_content in response_content:
        image_datetime, image_name = (
            image_content['date'],
            image_content['image']
            )
        img_date = datetime.fromisoformat(image_datetime).strftime('%Y/%m/%d')
        image_url = ('https://api.nasa.gov/EPIC/archive/natural/'
                    f'{img_date}/png/{image_name}.png')
        request_image_url_params = {
            'api_key': nasa_token,
        }
        response_selected_image = requests.get(
            image_url,
            params=request_image_url_params
            )
        response_selected_image.raise_for_status()
        nasa_epic_images.append(response_selected_image.url)
    for link in nasa_epic_images:
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
        'response_content_count',
        type=int,
        help='Count of content response.'
        )
    parser.add_argument(
        'content_path',
        type=str,
        help='Name of the content path.'
        )
    args = parser.parse_args()
    get_and_save_nasa_epic_images(
        nasa_token,
        args.response_content_count,
        args.content_path
        )
