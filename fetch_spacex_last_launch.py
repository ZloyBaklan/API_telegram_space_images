import requests


def fetch_spacex_last_launch(flight_id):
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    params = {
        # 'id': f'{flight_id}', - не воспринимает, выводит все вылеты...
    }
    response = requests.get(content_url, params=params)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    flight_id = '5eb87d47ffd86e000604b38a'
    spacex_images_database = []
    for i in fetch_spacex_last_launch(flight_id):
        spacex_images_database.append(i)

'''
Вопрос по всем fetch_..., если я так делаю запрос,
и функция более не возвращает выборку фотографий, а формируется она в мейн
Как же другие функции, например для сохранения изображений
или для определения формата эту выборку получат?
'''