import numpy as np

# Creating a matrix
A = np.array([[1, 2], [3, 4]])
print("Matrix A:\n", A)

# Matrix properties
A_shape = A.shape           # Shape of the matrix
transpose_A = A.T           # Transpose of the matrix
det_A = np.linalg.det(A)    # Determinant (only for square matrices)
inverse_A = np.linalg.inv(A) # Inverse (only if the matrix is invertible)

B = np.array([[5, 6], [7, 8]])
# Matrix multiplication
C = np.dot(A, B)
# or equivalently
C = A @ B
print("Matrix Multiplication A @ B:\n", C)


# Example system: Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solving for x
x = np.linalg.solve(A, b)
print("Solution vector x:", x)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
