import numpy as np

## 01 ##
a = np.array([[1, 2], [3, 4], [5, 6]])

print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
print(a[[0, 1, 2], [0, 1, 0]])

## 02 ##
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print("1)\n", x + y)
print("2)\n", np.add(x, y))
print("3)\n", np.subtract(x, y))
print("4)\n", np.multiply(x, y))
print("5)\n", np.divide(x, y))
print("6)\n", np.dot(x, y))

## 03 ##
z = np.array([[1, 2], [3, 4]])

print("1)\n", np.sum(z))
print("2)\n", np.sum(z, axis=0))
print("3)\n", np.sum(z, axis=1))

