import os
import time
import telegram
import random

from dotenv import load_dotenv
from random import randint

from publish_image_to_telegram import publish_image_to_telegram
from fetch_spacex_last_launch import fetch_spacex_last_launch
from fetch_nasa_space_images import nasa_space_img
from fetch_nasa_epic_images import nasa_epic_images
from optimize_and_save_image import optimize_size_of_images


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    content_path = 'images'
    flight_id = '5eb87d47ffd86e000604b38a'
    counter_nasa = randint(1, 50)
    counter_epic = 2
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    chat_id = updates[-1].channel_post.chat.id
    while True:
        fetch_spacex_last_launch(flight_id, content_path)
        nasa_epic_images(nasa_token, counter_epic, content_path)
        nasa_space_img(nasa_token, counter_nasa, content_path)
        optimize_size_of_images(content_path)
        set_of_images = os.listdir(content_path)
        while set_of_images != []:
            chosen_image = random.choice(set_of_images)
            set_of_images.remove(chosen_image)
            with open(f'{content_path}/' + chosen_image, 'rb') as photo:
                publish_image_to_telegram(photo, chat_id, bot)
            time.sleep(float(publication_frequency))
