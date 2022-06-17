import requests
from optimize_and_save_image import save_images_to_path, define_image_format


def fetch_spacex_last_launch(flight_id, content_path):
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    params = {}
    response = requests.get(content_url, params=params)
    response.raise_for_status()
    image_url = response.json()['links']['flickr']['original']
    defined_images = define_image_format(image_url)
    image_names, image_formats = (list(defined_images.keys()),
                                  list(defined_images.values()))
    save_images_to_path(image_url, content_path, image_names, image_formats)


if __name__ == '__main__':
    flight_id = '5eb87d47ffd86e000604b38a'
    content_path = 'images'
    fetch_spacex_last_launch(flight_id, content_path)
