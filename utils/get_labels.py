"""
Gets labels needed for modelling from a given file
"""

import pandas as pd


def get_labels(file_path: str, subset: int = 0):
    """
    Gets labels needed for modelling from a given file
    :return: a numpy array of labels
    """

    lab_pd = pd.read_csv(file_path)

    if subset != 0:
        lab_np = (
            lab_pd[0:subset][
                [
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
                ]
            ]
            .to_numpy()
            .astype("int")
            + 1
        ) / 2
    else:
        lab_np = (
            lab_pd[
                [
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
                ]
            ]
            .to_numpy()
            .astype("int")
            + 1
        ) / 2

    return lab_np
