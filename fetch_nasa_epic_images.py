import os
import requests

from dotenv import load_dotenv
from datetime import datetime

from optimize_and_save_image import save_images_to_path, define_image_format


def nasa_epic_images(nasa_token, content_count, content_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_token,
    }
    response = requests.get(epic_url,  params=params)
    response.raise_for_status()
    nasa_epic_images_database = []
    response_content = response.json()[:content_count]
    for image_content in response_content:
        image_datetime, image_name = (
            image_content['date'],
            image_content['image']
            )
        img_date = datetime.fromisoformat(image_datetime).strftime('%Y/%m/%d')
        main_url = ('https://api.nasa.gov/EPIC/archive/natural/'
                    f'{img_date}/png/{image_name}.png')
        params_main = {
            'api_key': nasa_token,
        }
        response_main = requests.get(main_url,  params=params_main)
        response_main.raise_for_status()
        nasa_epic_images_database.append(response_main.url)
    for link in nasa_epic_images_database:
        defined_image_name, defined_image_format = define_image_format(link)
        save_images_to_path(
            link,
            content_path,
            defined_image_format,
            defined_image_name
            )


if __name__ == '__main__':
    load_dotenv()
    content_count = 2
    nasa_token = os.getenv('NASA_TOKEN')
    content_path = 'images'
    nasa_epic_images(nasa_token, content_count, content_path)
