import os
import requests
import PIL
import PIL.Image

from pathlib import Path
from urllib.parse import urlparse, unquote


'''
Скрипты для оптимизации размеров(optimize_size_of_images)
и сохранения фотографий(save_images_to_path).
Необходимо задать директорию,
в которую будет сохранятся контент с API запросов, например:
```
content_path = 'images'
```
Формат и названия изображений можно задать, а можно получить из пункта 4.
Скрипт получает на вход [content]
- где контент это выборка фотографий полученных с API сервисов.
Функция сохраняет изображения в указанную директорию
с нужными форматами и названиями.
Опционально можно подогнать все изображения в директории под один размер.
'''


def save_images_to_path(link, content_path, image_format, image_name):
    Path(content_path).mkdir(parents=True, exist_ok=True)
    filename = f'{image_name}{image_format}'
    with open(os.path.join(content_path, filename), 'wb') as image:
        response = requests.get(link)
        response.raise_for_status()
        image.write(response.content)


def optimize_size_of_images(photo_address):
    try:
        with PIL.Image.open(photo_address) as full_size_img:
            full_size_img.thumbnail((1000, 1000))
    except PIL.UnidentifiedImageError:
        os.remove(photo_address)


'''
Скрипт для опрделения формата и названия фотографий с API ответов.
Скрипт получает на вход [content] - имеющаяся выборка изображений
( которые могут быть разного формата: png,jpg и т д),
скрипт возврщает выборку изображений в формате словаря,
где ключ это имя, а формат - значение.
Данный скрипт нужен, чтобы функция сохранения фото
понимала в каком формате сохранять изображение
и использовала оригинальное название(опционально).
'''


def define_image_format(link):
    image_name = os.path.split(urlparse(link).path)
    image_info = os.path.splitext(unquote(image_name[-1]))
    return image_info
