import numpy as np
def ortho(v):
    n = len(v)
    a = np.zeros((n, n))
    for i in range(n):
        a[i] = v[i]
        for j in range(i):
            a[i] -= np.dot(v[i], a[j]) / np.dot(a[j], a[j]) * a[j]
        a[i] /= np.linalg.norm(a[i])
    return a
vectors = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
a = ortho(vectors)
print(a)