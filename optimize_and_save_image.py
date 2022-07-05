import os
import requests
import PIL
import PIL.Image

from pathlib import Path
from urllib.parse import urlparse, unquote


def save_images_to_path(link, content_path, image_format, image_name):
    '''

    Скрипт сохранения фотографий(save_images_to_path).
    Необходимо задать директорию,
    в которую будет сохранятся контент с API запросов, например:
    ```
    content_path = 'images'
    ```
    Формат и названия изображений можно также задать,
    а можно получить из спецаильной функции define_image_format.

    Скрипт получает на вход ссылку на изображение [link]
    - полученную с API сервисов.

    Функция сохраняет изображение в указанную директорию
    с "нужным" форматом и названием.

    '''

    Path(content_path).mkdir(parents=True, exist_ok=True)
    filename = f'{image_name}{image_format}'
    response = requests.get(link)
    response.raise_for_status()
    with open(os.path.join(content_path, filename), 'wb') as image:
        image.write(response.content)


def optimize_size_of_images(photo_address):
    '''

    Данная функция предназначена для
    оптимизации размеров(optimize_size_of_images).
    Опционально можно подогнать все изображения в директории под один размер,
    а также проверить не поврежден ли файл
    и является ли он изображением с "верным" форматом.

    На вход подается путь к изображению в файловой системе,
    если изображение неверного формата или повреждено,
    оно удаляется из директории.
    Если все в порядке изображение "оптимизируется по размерам".

    '''
    try:
        with PIL.Image.open(photo_address) as full_size_img:
            full_size_img.thumbnail((1000, 1000))
    except PIL.UnidentifiedImageError:
        os.remove(photo_address)


def define_image_format(link):
    '''

    Скрипт для определения формата и названия фотографий с API ответов.

    Скрипт получает на вход ссылку [link] - на изображение
    (которое может быть разного формата: png,jpg и т д).

    Скрипт возвращает формат и "истинное" название изображения.

    Данный скрипт нужен, чтобы функция сохранения фото
    понимала в каком формате сохранять изображение
    и использовала оригинальное название(опционально).

    '''

    image_full_name = os.path.split(urlparse(link).path)
    image_name_and_format = os.path.splitext(unquote(image_full_name[-1]))
    return image_name_and_format
