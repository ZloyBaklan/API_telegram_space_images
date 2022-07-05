import argparse
import os
import time
import telegram
import random

from dotenv import load_dotenv
from random import randint

from publish_image_to_telegram import publish_image_to_telegram
from fetch_spacex_last_launch import fetch_and_save_spacex_last_launch
from fetch_nasa_space_images import get_and_save_nasa_space_img
from fetch_nasa_epic_images import get_and_save_nasa_epic_images
from optimize_and_save_image import optimize_size_of_images


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    chat_id = os.getenv('CHAT_ID')
    parser = argparse.ArgumentParser(description='Argeuments for script.')
    parser.add_argument(
        'flight_id',
        type=str,
        help='Enter the ID of the flight you want to get a photos from.'
        )
    parser.add_argument(
        'content_path',
        type=str,
        help='Name of the content path.'
        )
    parser.add_argument(
        'content_nasa_response_count',
        type=int,
        help='Count of response links for nasa API.'
        )
    parser.add_argument(
        'content_epic_response_count',
        type=int,
        help='Count of response links for nasa epic API.'
        )
    args = parser.parse_args()
    while True:
        fetch_and_save_spacex_last_launch(args.flight_id, args.content_path)
        get_and_save_nasa_epic_images(
            nasa_token,
            args.content_epic_response_count,
            args.content_path
            )
        get_and_save_nasa_space_img(
            nasa_token,
            args.content_nasa_response_count,
            args.content_path
            )
        set_of_images = os.listdir(args.content_path)
        for filename in set_of_images:
            photo_address = f'{args.content_path}/{filename}'
            optimize_size_of_images(photo_address)
        while set_of_images:
            chosen_image = random.choice(set_of_images)
            set_of_images.remove(chosen_image)
            file_path = f'{args.content_path}/{chosen_image}'
            try:
                publish_image_to_telegram(file_path, chat_id, telegram_token)
            except telegram.error.BadRequest:
                print('Файл поврежден или неверный формат изображения.')
            time.sleep(float(publication_frequency))
