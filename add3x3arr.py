#  Write a Python Program to add two arrays each of dimension 3,3 
import numpy as np
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

array2 = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

print("array1\n",array1)
print("array2\n",array2)

sumArray=array1+array2
print("sum\n",sumArray)



'''
out:-
array1
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
array2
 [[9 8 7]
 [6 5 4]
 [3 2 1]]
sum
 [[10 10 10]
 [10 10 10]
 [10 10 10]]  '''