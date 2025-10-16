#np.arrary
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#np.zeros
zeros_array = np.zeros((3, 4))
print(zeros_array)

#np.ones
ones_array = np.ones((2, 3))
print(ones_array)

#np.sum
sum_array = np.sum(arr)
print(sum_array)

#np.linspace
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)

#np.reshape
reshaped_array = np.reshape(arr, (5, 1))
print(reshaped_array)

#np.concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.concatenate((a, b)))

#np.split
split_array = np.array([1, 2, 3, 4, 5, 6])
print(np.split(split_array, 3))

#np.transpose
matrix = np.array([[1, 2], [3, 4]])
print(np.transpose(matrix))

#np.dot
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print(np.dot(matrix_a, matrix_b))
