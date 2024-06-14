import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[1,2,3],
              [4,5,6]])

print(b.T) # transpose of b
d = b.T
print("-------------------")
c = np.matmul(a,d) #matrix multiplication
print(c)