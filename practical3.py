import numpy as np
a=np.array([[1,3,4],[4,3,5],[5,7,6]])
print("your matrix is\n",a,)

d = np.linalg.det(a)
print("\ndeterminant of given matrix is:- ", int(d))

co=np.linalg.inv(a).T * d
print("\ncofactor matrix of the given matrix is\n",co)

inv=np.linalg.inv(a)
print("\ninverse of given matrix:- \n",inv)

tran = co.transpose()
print("\nadjoint of given matrix:- \n",tran)

