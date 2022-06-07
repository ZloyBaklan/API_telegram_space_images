import os
from urllib.parse import urlparse, unquote


def define_image_format(content):
    defined_images_database = {}
    for i in content:
        image_name = os.path.split(urlparse(i).path)
        image_format = os.path.splitext(unquote(image_name[-1]))
        defined_images_database[image_format[0]] = image_format[-1]
    return defined_images_database
