import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from bs4 import BeautifulSoup
import PIL
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import tensorflow as tf


def getLables():
    annotations = sorted(list(os.listdir("data/annotations")))
    lables = []

    idx = 0

    for val in annotations:
        file_lable = 'maksssksksss' + str(idx) + '.xml'
        lable_path = os.path.join("data/annotations/", file_lable)
        with open(lable_path) as f:
            tempLable = []
            data = f.read()
            soup = BeautifulSoup(data, "xml")
            objects = soup.find_all("object")

            for obj in objects:
                if obj.find('name').text == "with_mask":
                    tempLable.append(1)
                elif obj.find('name').text == "mask_weared_incorrect":
                    tempLable.append(2)
                else:
                    tempLable.append(0)
            lables.append(tempLable)
        idx += 1

    return lables

def getImageVectors():
    images = sorted(list(os.listdir("data/images")))
    annotations = sorted(list(os.listdir("data/annotations")))
    Ximages = []

    idx = 0

    for img in images:
        file_image = 'maksssksksss' + str(idx) + '.png'
        image_path = os.path.join("data/images/", file_image)

        img_data = PIL.Image.open(image_path)
        img_arr = np.array(img_data)
        Ximages.append(img_arr)

        idx += 1

    return (Ximages)

