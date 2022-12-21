import numpy as np
from sympy import Matrix
  
M = Matrix([[1,3,4], [2,3,4], [5,7,8]])
print("Matrix : {} ".format(M))
    
M_rref = M.rref()  
      
print("The Row echelon form of matrix : {}".format(M_rref))

my_matrix = np.array([[1,3,4], [2,3,4], [5,7,8]])
print(my_matrix)
rank = np.linalg.matrix_rank(my_matrix)
print("Rank of the given Matrix is : ",rank) 
