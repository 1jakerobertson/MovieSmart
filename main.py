import numpy as np

# Create a 1D NumPy array (representing your 1D vector/data)
one_d_vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Reshape it into a 2D array (e.g., a 3x3 matrix)
# The -1 in reshape automatically calculates the dimension
# based on the other specified dimension.
two_d_sensor = one_d_vector.reshape((3, -1))

print("Original 1D vector:")
print(one_d_vector)
print("\nConverted 2D 'sensor' representation:")
print(two_d_sensor)