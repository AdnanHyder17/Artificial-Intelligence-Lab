# Use NumPy library and perform following tasks:
# 1. Initialize 2 arrays and add their contents.
# 2. Multiply all contents within one of the above arrays by an integer.
# 3. Reshape one of the arrays to be 2D (if existing array is 2D, make it 3D).
# 4. Convert One of the arrays to be of a different Data type.
# 5. Generate a sequence of numbers in the form of a NumPy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
# 6. From 2 NumPy arrays, extract the indexes in which the elements in the 2 arrays match.

import numpy as np

# 1: Initialize 2 arrays and add their contents
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result1 = array1 + array2
print("Task 1 Result:", result1)

# 2: Multiply all contents within one of the arrays by an integer
array3 = np.array([7, 8, 9])
multiplier = 2
result2 = array3 * multiplier
print("Task 2 Result:", result2)

# 3: Reshape one of the arrays to be 2D or 3D
array4 = np.array([[10, 11], [12, 13]])
if array4.ndim == 1:
    reshaped_array = array4.reshape(2, -1) # Reshape to be a 2D array
else:
    reshaped_array = array4.reshape(2, -1, 1) # Reshape to be a 3D array
print("Task 3 Result:", reshaped_array)

# 4: Convert one of the arrays to a different data type
array5 = np.array([14.5, -3.7, 8.9])
converted_array = array5.astype(int)
print("Task 4 Result:", converted_array)

# 5: Generate a sequence of numbers with gaps of two using NumPy arange function
sequence_array = np.arange(0,101,2)
print("Task 5 Result:", sequence_array)

# 6: Extract indexes where elements in two arrays match
array6 = np.array([1, 2, 3])
array7 = np.array([3, -1 ,5])
matching_indexes = np.where(array6 == array7)
print("Task 6 Result:", matching_indexes)
