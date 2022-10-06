# Imports
import pandas as pd
from pathlib import Path
from PIL import Image
import numpy as np
import os, sys

# Define paths/directories
image_dir_path = 'D:/manoo/Pictures/Camera Roll/'
dirs = os.listdir(image_dir_path)
new_path = 'D:/manoo/Pictures/DataAcademy/'

# Resize and save images
def resize():
    for item in dirs:
        if os.path.isfile(image_dir_path + item):
            im = Image.open(image_dir_path + item)
            f, e = os.path.splitext(new_path + item)
            imResize = im.resize((218, 178), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()

# Create temporary dataframe of predictions - change this to predictions from model
paths = [path.parts[-1:] for path in
         Path(new_path).glob('*.jpg')]
d = {'Images': paths, 'Prediction1': np.random.randint(0,100,size=(len(paths))), 'Prediction2': np.random.randint(0,100,size=(len(paths)))}
df = pd.DataFrame(data=d)

# Save predictions to csv
df.to_csv('D:/manoo/Output/predictions.csv')





