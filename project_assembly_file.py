import os
import time
import telegram
import random

from dotenv import load_dotenv
from random import randint

from publish_image_to_telegram import publish_image_to_telegram
from fetch_spacex_last_launch import fetch_spacex_last_launch
from fetch_nasa_space_images import get_nasa_space_img
from fetch_nasa_epic_images import get_nasa_epic_images
from optimize_and_save_image import optimize_size_of_images


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    content_path = 'images'
    flight_id = '5eb87d47ffd86e000604b38a'
    content_nasa_response_count = 25
    content_epic_response_count = 2
    chat_id = os.getenv('CHAT_ID')
    while True:
        fetch_spacex_last_launch(flight_id, content_path)
        get_nasa_epic_images(
            nasa_token,
            content_epic_response_count,
            content_path
            )
        get_nasa_space_img(
            nasa_token,
            content_nasa_response_count,
            content_path
            )
        set_of_images = os.listdir(content_path)
        for filename in set_of_images:
            photo_address = f'{content_path}/{filename}'
            optimize_size_of_images(photo_address)
        while set_of_images:
            chosen_image = random.choice(set_of_images)
            set_of_images.remove(chosen_image)
            file_path = f'{content_path}/{chosen_image}'
            try:
                publish_image_to_telegram(file_path, chat_id, telegram_token)
            except telegram.error.BadRequest:
                print('Файл поврежден или неверный формат изображения.')
            time.sleep(float(publication_frequency))
