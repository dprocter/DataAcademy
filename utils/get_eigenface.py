import PIL

import numpy as np
from PIL import Image
import os

def get_eigenface(directory_in:str, directory_out:str, iter: int = 1):

    allfiles = os.listdir(directory_in)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]

    w,h = Image.open(f"{directory_in}/{imlist[0]}").size
    N = len(imlist)

    arr = np.zeros((h,w,3), np.float)

    for im in imlist:
        imarr = np.array(Image.open(f"{directory_in}/{im}"), dtype = np.float)
        arr = arr+imarr

    arr = np.array(np.round(arr/N), dtype = np.uint8)

    out = Image.fromarray(arr, mode = "RGB")
    out.save(f"{directory_out}/eigenface{iter}.png")