"""
Runs predictions live over every photo the camera has taken
"""

import time
import pandas as pd
from utils.clear_folder import clear_folder
from utils.resize_image_dir import resize
from utils.get_predictions import get_predictions
from utils.get_eigenface import get_eigenface

def run_live_predictions(camera_path: str, resize_path: str, prediction_path: str, model_path: str, eigenface_path: str
                         ,lookalike_path: str, lookalike_model_path: str
                         , num_iterations = 100):

    clear_folder(prediction_path)
    clear_folder(eigenface_path)
    clear_folder(lookalike_path)

    for i in range(0,num_iterations):

        out_num = ""
        if i < 10:
            out_num += f"000{i}"
        elif i > 9 and i < 100:
            out_num += f"00{i}"
        elif i > 99:
            out_num += f"0{i}"
        else:
            out_num += f"{i}"

        clear_folder(f"{resize_path}/images_resized/")

        resize(camera_path, f"{resize_path}/images_resized/")

        out = get_predictions(resize_path, model_path)
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

        out.to_csv(f"{prediction_path}predictions{out_num}.csv")

        lookalikes = get_predictions(resize_path, lookalike_model_path)

        pd.DataFrame(lookalikes).to_csv(f"{lookalike_path}predictions{out_num}.csv")

        get_eigenface(directory_in=f"{resize_path}/images_resized", directory_out=eigenface_path, iter = out_num)

        time.sleep(1)

