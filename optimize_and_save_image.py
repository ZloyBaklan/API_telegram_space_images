import os
import requests
from pathlib import Path
from PIL import Image


def save_images_to_path(file, content_path, image_names, image_formats):
    filename = f'{image_names[count]}_{count}{image_formats[count]}'
    with open(os.path.join(content_path, filename), 'wb') as image:
        image.write(requests.get(file).content)


def optimize_size_of_images(content_path):
    content = os.listdir(content_path)
    for filename in content:
        with Image.open(f'{content_path}/{filename}') as full_size_image:
            full_size_image.thumbnail((1000, 1000))


if __name__ == '__main__':
    content_path = 'images'
    Path(content_path).mkdir(parents=True, exist_ok=True)
    count = 0
    content = []
    image_names, image_formats = '', ''
    '''
    content - должен быть выборкой изображений(ссылок),
    представление его во вспомогательном скрипте - не возможно.
    image_names/formats так же являются наборами внешней функции:
    define_image_format - поэтому в данном вспомогательном 
    обособленном скрипте им неоткуда взяться
    опять же возможно я не правильно понял комментарий...
    '''
    for file in content:
        save_images_to_path(file, content_path, image_names, image_formats)
        count+=1
