"""
Clears the contents of a folder
"""

import os

def clear_folder(folderpath: str):
    """
    Clears the contents of a folder
    :param folderpath: str, path to the folder you want to clear
    :return:
    """
    for f in os.listdir(folderpath):
        os.remove(os.path.join(folderpath, f))