from run_predictions import run_predictions

labels, preds = run_predictions("C:/Github/DataAcademy/data", "C:/Github/DataAcademy/data/models/fit_mutlilabel_model.h5", "C:/Github/DataAcademy/data/list_attr_celeba.csv")


from run_model import run_model
run_model(50)

from run_model import run_model
run_model(100, "C:/Github/DataAcademy/data")

#########################
import tensorflow as tf
from utils.import_data import import_data
from utils.get_labels import get_labels

model = tf.keras.models.load_model("C:/Github/DataAcademy/data/models/fit_mutlilabel_model.h5")

labs = get_labels("C:/Github/DataAcademy/data/list_attr_celeba.csv")

data = import_data(directory = "C:/Github/DataAcademy/data",subset = "validation",
                   labels = list(labs))

#################

tf.keras.preprocessing.image_dataset_from_directory(
        "C:/Github/DataAcademy/data",
        validation_split=0.2,
        subset="validation",
        seed=1337,
        image_size=(218, 178),
        batch_size=32,
        labels=None,
    )

######################

import pandas as pd
from utils.resize_image_dir import resize
resize("C:/Users/dproc/Pictures/Camera Roll/","C:/Github/DataAcademy/predictions/predict_me/images_resized/")

from utils.get_predictions import get_predictions

out = get_predictions("C:/Github/DataAcademy/predictions/predict_me", "C:/Github/DataAcademy/data/models/fit_mutlilabel_model.h5")
out = pd.DataFrame(out, columns=[
                    "Bald",
                    "Black_Hair",
                    "Blond_Hair",
                    "Brown_Hair",
                    "Gray_Hair",
                    "Smiling",
                    "Straight_Hair",
                    "Wavy_Hair",
                    "Wearing_Hat",
                    "Wearing_Earrings",
                    "Wearing_Necktie",
                    "Eyeglasses"
                ])

out.to_csv("C:/Github/DataAcademy/predictions/output/predictions.csv")

###############

from run_live_predictions import run_live_predictions
run_live_predictions(camera_path = "C:/Users/dproc/Pictures/Camera Roll/"
                     ,resize_path= "C:/Github/DataAcademy/predictions/predict_me"
                     , prediction_path="C:/Github/DataAcademy/predictions/output/"
                     , model_path= "C:/Github/DataAcademy/data/models/fit_mutlilabel_model.h5"
                     ,num_iterations = 5)