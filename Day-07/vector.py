import numpy as np 

v= np.array([37, 10, 7])

print("Vector v:", v)


v_length = np.linalg.norm(v)
unit_v = v / v_length 

dot_product = np.dot(v,v)