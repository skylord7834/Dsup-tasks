# Write a Python Program to add one vector(1d array with 3 elements) with an array of 
# dimension 3,3 
import numpy as np

vector = np.array([1, 2, 3])

array3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
result=array3x3+vector
print(result)

'''
out-
[[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]
 '''