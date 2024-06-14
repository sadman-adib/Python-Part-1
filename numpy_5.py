# Argmax/min find max/min are at which indices

import numpy as np

a = np.array([21,2,-35,-4,5,66,-72,8,9])

b = np.array([[1, 4],
              [6, 2],
              [3, 5]])

print(a.argmax())
print(b.argmax())

print("Column Wise", b.argmax(axis = 0))
print("Row Wise", b.argmax(axis = 1))