import numpy as np

# Load the .npz file
# Replace 'your_file.npz' with the actual path to your .npz file
data = np.load('your_file.npz')

# List the keys (array names) within the .npz file
print("Arrays in the .npz file:", data.files)

# Access individual arrays by their key
# For example, if 'arr_0' is one of the array names:
array_content = data['arr_0']
print("Content of 'arr_0':\n", array_content)

# You can iterate through all arrays if you don't know the names beforehand
for key in data.keys():
    print(f"\nContent of '{key}':\n", data[key])

# Close the NpzFile instance to release resources
data.close()