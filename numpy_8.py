# sum(3*3 + -5*-5 + 0*5) > 0

import numpy as np

a = np.array([3, -5, 2, 9, 0, 7])
b = np.array([3, -5, -2, -1, 5, -1])

c = a*b
print(c)

d = c[c>0]
print(d)

print(d.sum())