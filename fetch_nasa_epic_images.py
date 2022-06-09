import os
import datetime
import requests

from dotenv import load_dotenv

def nasa_epic_images(nasa_token, counter):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': f'{nasa_token}',
    }
    response = requests.get(epic_url,  params=params)
    nasa_epic_images_database = []
    response_content = response.json()[0:counter]
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
        nasa_epic_images_database.append(response_main.url)
    return nasa_epic_images_database


if __name__ == '__main__':
    load_dotenv()
    counter = 6
    nasa_token = os.getenv('NASA_TOKEN')
