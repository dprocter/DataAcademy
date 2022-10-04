"""
runs predictions on a given directory
"""
import tensorflow as tf

from utils.import_data import import_data


def run_predictions(img_dir, model_path, output_path):

    model = tf.keras.models.load_model(model_path)

    data = import_data(directory=img_dir, subset=None, labels=None)

    preds = model.predict(data)
