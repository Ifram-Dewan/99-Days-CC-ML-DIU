import numpy as np

# Creating arrays
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

# Array operations
array2 = array * 2
print("Array multiplied by 2:", array2)

# Statistical methods
mean = np.mean(array)
print("Mean:", mean)

# Reshaping an array
reshaped_array = np.reshape(array, (5, 1))
print("Reshaped Array:\n", reshaped_array)

# Broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix + 10:\n", matrix + 15)
