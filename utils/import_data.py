"""
Imports a directory of files and outputs a dataset
"""

import tensorflow as tf


def import_data(directory, subset, labels):
    """
    Imports a directory of files and outputs a dataset

    :return: a tf.dataset
    """

    if subset is None:
        validation_split = None
    else:
        validation_split = 0.2

    output_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        validation_split=validation_split,
        subset=subset,
        seed=1337,
        image_size=(218, 178),
        batch_size=32,
        labels=labels,
    )

    return output_dataset
