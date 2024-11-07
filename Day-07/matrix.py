

import numpy as np 

# Creating a matrix
A = np.array([[1, 2], [3, 4]])

print("Ifram Item:\n", A) #just kidding with code [ifram item mean matrix]


# Matrix properties

A_shape = A.shape           # Shape of the matrix


transpose_A = A.T           # Transpose of the matrix


det_A = np.linalg.det(A)    # Determinant (only for square matrices)

inverse_A = np.linalg.inv(A) # Inverse (only if the matrix is invertible)
