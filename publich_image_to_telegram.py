import os
import telegram
import random
import requests

from dotenv import load_dotenv

def publish_image_to_telegram(photo, chat_id):
    if photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption='Свежий дроп')


''' 
По-помему код стал странный, либо я не понял что необходимо вынести...
'''
if __name__ == '__main__':
    load_dotenv()
    content_path = 'images'
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    set_of_images = os.listdir(content_path)
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    chat_id = updates[-1].channel_post.chat.id
    while set_of_images != []:
        chosen_image = random.choice(set_of_images)
        set_of_images.remove(chosen_image)
        with open(f'{content_path}/' + chosen_image, 'rb') as photo:
            publish_image_to_telegram(photo, chat_id)
