import pydicom
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import re

#constants
pattern = re.compile(r'IM\d+')

# Read a DICOM file
ds = pydicom.dcmread("/Users/katherine/PycharmProjects/breast_cancer/dataset-uta4-dicom/dataset/mm/p1_d045f565-e0be-432c-aaab-8296b169c529/IM0")

# Now you can access the dataset attributes
print("Patient Name:", ds.PatientName)
print("Modality:", ds.Modality)
print("Image Size:", ds.Rows, "x", ds.Columns)
print("Patient ID:", ds.PatientID) # Ex
print(ds)


image_data = ds.pixel_array
print(image_data)

#plt.imshow(image_data, cmap=plt.cm.bone)
#plt.title("DICOM Image")
#plt.show()

dir_path = "/Users/katherine/PycharmProjects/breast_cancer/dataset-uta4-dicom/dataset/mm/p1_d045f565-e0be-432c-aaab-8296b169c529/"
dicom_datasets = []

for root, _, filenames in os.walk(dir_path):
    for filename in filenames:
        dcm_path = Path(root, filename)
        if pattern.search(dcm_path.stem):
            try:
                ds = pydicom.dcmread(dcm_path, force=True) # force=True handles cases where the dataset might not be strictly compliant
                dicom_datasets.append(ds)
            except IOError as e:
                print(f"Can't import {dcm_path.stem}: {e}")

# Now you have a list of DICOM datasets in `dicom_datasets`
# You can iterate through this list to access each dataset's attributes.
#example of accessing specific attributes
print(len(dicom_datasets))
n_images = len(dicom_datasets)

fig, axes = plt.subplots(26, n_images, figsize=(26 * n_images, 5))

#for i in range(n_images):
#    plt.imshow(dicom_datasets[i].pixel_array)
#plt.show()

"""for i in range(n_images):
    ax = axes[i]
    ax.imshow(dicom_datasets[i].pixel_array, cmap=plt.cm.bone)
    ax.set_title(f"Image {dicom_datasets[i].SOPInstanceUID}")
    ax.axis('off')

plt.tight_layout()
plt.show()"""