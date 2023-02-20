import numpy as np
from scipy.linalg import null_space, orth
  
M = np.array([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
  # Compute the basis of column space
a= orth(M.T)

    # Compute the basis of null space
b= null_space(M)

    # Compute the basis of row space
c= orth(M)

    # Compute the basis of left null space
d= null_space(M.T)

print(a,"are the basis of column space\n")
print(b,"are the basis of null space\n")
print(c,"are the basis of row space\n")
print(d,"are the basis of the left null space\n")
