import numpy as np

b = np.array([[1, 4, 9, 10],
              [6, 2, -1, -8],
              [3, -5, 2, 15],
              [31, 5, 12, -5]])

print(b[1][2])
print("-------------------")
print(b[0:2]) # first two rows
print("-------------------")
print(b[0:2, :]) # first two rows
print("-------------------")
print(b[:, 1:3]) # middle two columns
print("-------------------")
print(b[:, -1]) # last column
print("-------------------")
print(b[:, -2:]) # last two columns
print("-------------------")
print(b[:, 2:]) # after first two columns
print("-------------------")
print(b[1:3, 1:4]) # middle 4 elements
print("-------------------")