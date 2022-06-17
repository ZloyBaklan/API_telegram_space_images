import os
import datetime
import requests
from dotenv import load_dotenv

from optimize_and_save_image import save_images_to_path


def nasa_epic_images(nasa_token, counter, content_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': f'{nasa_token}',
    }
    response = requests.get(epic_url,  params=params)
    nasa_epic_images_database = {}
    response_content = response.json()[0:counter]
    image_formats = ['.png']*(counter+1)
    for image_content in response_content:
        image_datetime, image_name = (image_content['date'],
                                      image_content['image'])
        image_date = datetime.datetime.strptime(image_datetime,
                                                '%Y-%m-%d %H:%M:%S')
        main_url = ('https://api.nasa.gov/EPIC/archive/natural/'
                    f'{image_date.strftime("%Y/%m/%d")}/png/{image_name}.png')
        params_main = {
            'api_key': f'{nasa_token}',
        }
        response_main = requests.get(main_url,  params=params_main)
        nasa_epic_images_database[image_name] = response_main.url
    save_images_to_path(list(nasa_epic_images_database.values()),
                        content_path, list(nasa_epic_images_database.keys()),
                        image_formats)


if __name__ == '__main__':
    load_dotenv()
    counter = 2
    nasa_token = os.getenv('NASA_TOKEN')
    content_path = 'images'
    nasa_epic_images(nasa_token, counter, content_path)
