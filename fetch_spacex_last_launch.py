import requests
from optimize_and_save_image import save_images_to_path, define_image_format


def fetch_spacex_last_launch(flight_id, content_path):
    content_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    request_params = {}
    response = requests.get(content_url, params=request_params)
    response.raise_for_status()
    set_of_links = response.json()['links']['flickr']['original']
    for link in set_of_links:
        defined_image_name, defined_image_format = define_image_format(link)
        save_images_to_path(
            link,
            content_path,
            defined_image_format,
            defined_image_name
            )


if __name__ == '__main__':
    flight_id = '5eb87d47ffd86e000604b38a'
    content_path = 'images'
    fetch_spacex_last_launch(flight_id, content_path)
