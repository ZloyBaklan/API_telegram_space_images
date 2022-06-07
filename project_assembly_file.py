import os
import time

from dotenv import load_dotenv

from publich_image_to_telegram import publish_image_to_telegram
from define_image_fromat import define_image_format
from fetch_spacex_last_launch import fetch_spacex_last_launch
from fetch_nasa_space_images import nasa_space_img
from fetch_nasa_epic_images import nasa_epic_images
from optimize_and_save_image import saving_images, size_optimization


def getting_images(flight_id, nasa_token, content_path):
    spacex_content = fetch_spacex_last_launch(flight_id)
    nasa_space_content = nasa_space_img(nasa_token)
    nasa_epic_content = nasa_epic_images(nasa_token)
    summary = spacex_content+nasa_epic_content+nasa_space_content
    defined_images = define_image_format(summary)
    image_names, image_formats = (list(defined_images.keys()),
                                  list(defined_images.values()))
    saving_images(summary, content_path, image_names, image_formats)


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    period_publications = os.getenv('PUBLICATION_FREQUENCY')
    content_path = 'images'
    flight_id = '5eb87d47ffd86e000604b38a'
    while True:
        getting_images(flight_id, nasa_token, content_path)
        size_optimization(content_path)
        time.sleep(float(period_publications))
        publish_image_to_telegram(content_path, telegram_token)
