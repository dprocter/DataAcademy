"""
runs the model we want
"""

from utils.get_celeb_labels import get_celeb_labels
from utils.import_data import import_data
from utils.fit_multiclass import fit_multiclass


def run_model(epochs:int, data_path = "C:/Github/DataAcademy/test_data", label_sample = 0):
    """
    runs the model we want
    """

    labels = get_celeb_labels("C:/Github/DataAcademy/data/identity_CelebA.csv", label_sample)

    train_ds = import_data(
        data_path, subset="training", labels=list(labels)
    )

    val_ds = import_data(
        data_path, subset="validation", labels=list(labels)
    )

    fit_multiclass(train=train_ds, val=val_ds, epochs=epochs, save_path=(f"{data_path}/models"))