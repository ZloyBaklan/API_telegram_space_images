import argparse
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
    # flight_id = '5eb87d47ffd86e000604b38a' - чтобы не потерять id с фото
    parser = argparse.ArgumentParser(description='Argeuments for script.')
    parser.add_argument(
        'flight_id',
        type=str,
        help='Enter the ID of the flight you want to get a photo from.'
        )
    parser.add_argument(
        'content_path',
        type=str,
        help='Name of the content path.'
        )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.flight_id, args.content_path)
