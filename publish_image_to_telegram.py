import os
import telegram
import random
import time

from dotenv import load_dotenv


def publish_image_to_telegram(file_path, chat_id, telegram_token):
    bot = telegram.Bot(token=telegram_token)
    with open(file_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption='Свежий дроп')


if __name__ == '__main__':
    load_dotenv()
    content_path = 'images'
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    set_of_images = os.listdir(content_path)
    chat_id = os.getenv('CHAT_ID')
    while set_of_images:
        chosen_image = random.choice(set_of_images)
        file_path = f'{content_path}/{chosen_image}'
        try:
            publish_image_to_telegram(file_path, chat_id, telegram_token)
        except telegram.error.BadRequest:
            print('Файл поврежден или неверный формат изображения.')
        time.sleep(float(publication_frequency))
        os.remove(file_path)
