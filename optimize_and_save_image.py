import os
import requests
from pathlib import Path
from PIL import Image


def saving_images(content, content_path, image_names, image_formats):
    Path(content_path).mkdir(parents=True, exist_ok=True)
    count = 0
    for i in content:
        filename = f'{image_names[count]}_{count}{image_formats[count]}'
        with open(os.path.join(content_path, filename), 'wb') as file:
            file.write(requests.get(i).content)
        count += 1


def size_optimization(content_path):
    content = os.listdir(content_path)
    for filename in content:
        full_size_image = Image.open(f'{content_path}/{filename}')
        full_size_image.thumbnail((1000, 1000))
