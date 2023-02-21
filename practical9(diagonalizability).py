import numpy as np


M= np.array([86, 4, 7, 12, 32, 72])

def divergence(a):
    return np.ufunc.reduce(np.add,np.gradient(a))

print("Your matrix:-\n ", M)

print("Divergence of this matrix:-:\n ",divergence(M))