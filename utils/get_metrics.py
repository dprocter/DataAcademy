"""
Takes labels and predictions and returns clasification metrics for each, as a csv
"""

import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, balanced_accuracy_score, roc_auc_score

def get_metrics(labels, predictions, output_path = "C:/Github/DataAcademy/data/metrics.csv"):
    """
    Takes labels and predictions and returns clasification metrics for each, as a csv
    :param labels: labels, an array containing 0 and 1
    :param predictions: predictions
    :return: nothing, it will write a csv
    """

    precision = [precision_score(labels[:,x], np.where(predictions[:,x]>0.5,1,0)) for x in range(0,12)]
    recall = [recall_score(labels[:,x], np.where(predictions[:,x]>0.5,1,0)) for x in range(0,12)]
    f1 = [f1_score(labels[:,x], np.where(predictions[:,x]>0.5,1,0)) for x in range(0,12)]
    balanced_acc = [balanced_accuracy_score(labels[:,x], np.where(predictions[:,x]>0.5,1,0)) for x in range(0,12)]
    auc = [roc_auc_score(labels[:,x], np.where(predictions[:,x]>0.5,1,0)) for x in range(0,12)]

    output_df = pd.DataFrame((precision,recall,f1,balanced_acc, auc),columns = [
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
                ],index = ["Precision", "Recall", "F1", "BalancedAccuracy", "AUC"]
    )

    output_df.to_csv(output_path)
