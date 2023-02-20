import numpy as np
def gauss_elimination(a, b):
    n = a.shape[0]
    for i in range(n):
        max_element = np.abs(A[i, i])
        max_row = i
        for k in range(i + 1, n):
            if np.abs(a[k, i]) > max_element:
                max_element = np.abs(a[k, i])
                max_row = k
        if max_row != i:
            a[[i, max_row]] = a[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        for k in range(i + 1, n):
            c = -a[k, i] / a[i, i]
            a[k, i:] = a[k, i:] + c * a[i, i:]
            b[k] = b[k] + c * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
    return x
A = np.array([[1, 2, 6], [0, 1, 4], [5, 6, 0]])
b = np.array([2, 2, 4])
x = gauss_elimination(A, b)
print("\nHomogeneous solution of given Equations is:")
print(x)

A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
b = np.array([2, 7, -20])
x = gauss_elimination(A, b)
print("\nNon-homogeneous solution of given Equations is:")
print(x)