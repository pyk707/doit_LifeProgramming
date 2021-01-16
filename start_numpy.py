import numpy as np

a = np.array([[2,3],[5,2]])
print(a)
print()
d = np.array([[1, 2, 3, 4, 5], [2, 4, 5, 6, 7], [5, 7, 8, 9, 9]])
print(d)
print()
print(d[2][4])
print()
print(d.shape)
print(d.dtype)
print()

data = np.arange(1,5)
print(data)
print(data.dtype)
print()

data.astype('float64')
print(data)