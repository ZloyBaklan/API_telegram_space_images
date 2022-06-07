import os
import telegram
import random


def publish_image_to_telegram(content_path, telegram_token):
    set_of_images = os.listdir(content_path)
    bot = telegram.Bot(token=telegram_token)
    updates = bot.get_updates()
    chat_id = updates[-1].channel_post.chat.id
    while set_of_images != []:
        chosen_image = random.choice(set_of_images)
        photo = open(f'{content_path}/' + chosen_image, 'rb')
        bot.send_photo(chat_id=chat_id, photo=photo, caption='Свежий дроп')
        set_of_images.remove(chosen_image)
    else:
        bot.send_message(text='Изображений больше нет, загружаем новые.')
