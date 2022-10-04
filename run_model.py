"""
runs the model we want
"""

from utils.get_labels import get_labels
from utils.import_data import import_data
from utils.fit_model import fit_model


def run_model(epochs:int):
    """
    runs the model we want
    """

    labels = get_labels("C:/Github/DataAcademy/data/list_attr_celeba.csv", 1000)

    train_ds = import_data(
        "C:/Github/DataAcademy/data", subset="training", labels=list(labels)
    )

    val_ds = import_data(
        "C:/Github/DataAcademy/data", subset="validation", labels=list(labels)
    )

    fit_model(train=train_ds, val=val_ds, epochs=epochs, save_path="C:/Github/DataAcademy/data/models")
