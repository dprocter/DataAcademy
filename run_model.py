"""
runs the model we want
"""

from utils.get_labels import get_labels
from utils.import_data import import_data
from utils.fit_multihead import fit_multihead


def run_model(epochs:int, data_path = "C:/Github/DataAcademy/data", label_sample = 0):
    """
    runs the model we want
    """

    labels = get_labels("C:/Github/DataAcademy/data/list_attr_celeba.csv", label_sample)

    train_ds = import_data(
        data_path, subset="training", labels=list(labels)
    )

    val_ds = import_data(
        data_path, subset="validation", labels=list(labels)
    )

    fit_multihead(train=train_ds, val=val_ds, epochs=epochs, save_path=(f"{data_path}/models"))
