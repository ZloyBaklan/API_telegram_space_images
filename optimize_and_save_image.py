import os
import requests
import PIL
import PIL.Image

from pathlib import Path
from urllib.parse import urlparse, unquote


def save_images_to_path(content, content_path, image_names, image_formats):
    Path(content_path).mkdir(parents=True, exist_ok=True)
    count = 0
    for file in content:
        filename = f'{image_names[count]}{image_formats[count]}'
        with open(os.path.join(content_path, filename), 'wb') as image:
            image.write(requests.get(file).content)
        count += 1


def optimize_size_of_images(content_path):
    content = os.listdir(content_path)
    for filename in content:
        try:
            with PIL.Image.open(f'{content_path}/{filename}') as full_size_img:
                full_size_img.thumbnail((1000, 1000))
        except PIL.UnidentifiedImageError:
            os.remove(f'{content_path}/{filename}')


def define_image_format(content):
    defined_images_database = {}
    for url in content:
        image_name = os.path.split(urlparse(url).path)
        image_format = os.path.splitext(unquote(image_name[-1]))
        defined_images_database[image_format[0]] = image_format[-1]
    return defined_images_database
