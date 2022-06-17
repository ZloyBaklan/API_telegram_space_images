import os
import telegram
import random
import time

from dotenv import load_dotenv


def publish_image_to_telegram(photo, chat_id, bot):
    if photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption='Свежий дроп')


if __name__ == '__main__':
    load_dotenv()
    content_path = 'images'
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY')
    set_of_images = os.listdir(content_path)
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    chat_id = updates[-1].channel_post.chat.id
    while set_of_images != []:
        chosen_image = random.choice(set_of_images)
        with open(f'{content_path}/' + chosen_image, 'rb') as photo:
            try:
                publish_image_to_telegram(photo, chat_id, bot)
            except telegram.error.BadRequest:
                bot.send_message(
                    chat_id=chat_id,
                    text='Файл поврежден или неверный формат изображения.'
                    )
        os.remove(f'{content_path}/' + chosen_image)
        time.sleep(float(publication_frequency))
