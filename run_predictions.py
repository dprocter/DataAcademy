"""
runs predictions on a given directory
"""
from utils.get_predictions import get_predictions
from utils.get_labels import get_labels
from utils.get_metrics import get_metrics


def run_predictions(img_dir, model_path, label_path):

    labels = get_labels(label_path, 5000)

    preds = get_predictions(img_dir, model_path)

    get_metrics(labels, preds)

    return(labels, preds)