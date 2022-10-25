"""
Gets labels needed for modelling from a given file
"""

import pandas as pd
import numpy as np
from keras.utils import np_utils

def get_celeb_labels(file_path: str, subset: int = 0):
    """
    Gets labels needed for modelling from a given file
    :return: a numpy array of labels
    """

    lab_pd = pd.read_csv(file_path, dtype = {"photo":np.str, "label": np.int})["label"]

    if subset != 0:
        lab_np = (
            lab_pd[0:subset,]
            .to_numpy()
        )
    else:
        lab_np = (
            lab_pd
            .to_numpy()
        )

    lab_np = np_utils.to_categorical(lab_np)

    return lab_np
