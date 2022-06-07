import requests


def fetch_spacex_last_launch(flight_id):
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    params = {
        # 'id': f'{flight_id}', - не воспринимает, выводит все вылеты...
    }
    response = requests.get(content_url, params=params)
    response.raise_for_status()
    filtered_response = response.json()['links']['flickr']['original']
    spacex_images_database = []
    for i in filtered_response:
        spacex_images_database.append(i)
    return spacex_images_database
