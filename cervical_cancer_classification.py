import numpy as np
import pandas as pd

import os

from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns

for dirname, _, filenames in os.walk('/Users/katherine/PycharmProjects/breast_cancer/cervical_cancer_data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

sns.set(style="whitegrid")

image_counts = {}

for category in categories:
    category_path = os.path.join(base_dir, category, category, "CROPPED")
    image_counts[category] = len([f for f in os.listdir(category_path) if f.endswith(('.bmp', '.jpg', '.png'))])

print(image_counts)

