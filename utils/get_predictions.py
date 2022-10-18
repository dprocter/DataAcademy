"""
gets predictions on a given directory from a given model
"""
from utils.import_data import import_data
import tensorflow as tf

def get_predictions(img_dir, model_path, subset = None, labels = None):

    model = tf.keras.models.load_model(model_path)

    data = import_data(directory=img_dir, subset= subset, labels=labels)

    return model.predict(data)