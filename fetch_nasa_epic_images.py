import datetime
import requests


def nasa_epic_images(nasa_token):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': f'{nasa_token}',
    }
    response = requests.get(epic_url,  params=params)
    nasa_epic_images_database = []
    response_content = response.json()[0:6]  # первые 7 записей
    for i in response_content:
        image_datetime, image_name = i['date'], i['image']
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
