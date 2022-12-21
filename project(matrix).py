import numpy as np

arr1 = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("Numpy Matrix is:")
print(arr1)
  
det = np.linalg.det(arr1)
print("Determinant of given 2X2 matrix:")
print(int(det))

tran = arr1.transpose()
print(f'Transposed Array:\n{tran}')
