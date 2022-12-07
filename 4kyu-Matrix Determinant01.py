import numpy as np

def determinant(matrix):

    array=np.array(matrix)

    det=np.linalg.det(array)

    return round(det)

print(determinant([[5]]))