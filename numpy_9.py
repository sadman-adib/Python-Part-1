#Given two 2d numpy arrays each representing a set of 2D points. 
# Find out the minimum distance between 
# two corresponding pair and its index

import numpy as np

a = np.array([[1, 1],
              [2, 2],
              [1, 3],
              [4, 3]])

b = np.array([[1, -1],
              [5, 2],
              [2, 3],
              [-1, 0]])

# Calculate the Euclidean distance for each corresponding pair
distances = np.linalg.norm(a - b, axis=1)

# Find the minimum distance and its index
min_distance_index = np.argmin(distances)
min_distance = distances[min_distance_index]

print("Minimum distance:", min_distance)
print("Index of minimum distance:", min_distance_index)