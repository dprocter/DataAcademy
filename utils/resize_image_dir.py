"""
Resizes all the images in a directory to what we want
"""
import re
import os
from glob import glob

from PIL import Image

def resize(image_dir_path: str, out_path):
    """

    :param image_dir_path: str, the directory of images you want to resize
    :return:
    """
#    files = os.listdir(image_dir_path)
    files = [f for f in os.listdir(image_dir_path) if f.endswith("jpg")]
#    files = glob("C:/Users/dproc/Pictures/Camera Roll/*.jpg")

    for item in files:
        im = Image.open(image_dir_path + item)
        f, e = os.path.splitext(out_path + item)
        imResize = im.resize((218, 178), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality=90)