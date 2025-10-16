import numpy as np
arr = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])
print("Array:\n", arr)
print("Element at depth 0, row 1, column 0:", arr[0, 1, 0])
print("Element at depth 1, row 0, column 1:", arr[1, 0, 1])