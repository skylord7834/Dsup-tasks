# Write a Python Program to multiply a vector(5 elements) with an array(dimension 5,2) 
import numpy as np

vector = np.array([1, 2, 3, 4, 5])
array5x2 = np.array([[1, 2],
                      [3, 4],
                      [5, 6],
                      [7, 8],
                      [9, 10]])
result=np.dot(vector,array5x2)
print("Vector:")
print(vector)
print("\n5x2 Array:")
print(array5x2)
print("\nResult:")
print(result)
print("dimension of the array is : ",result.shape)

'''
output:-
Vector:
[1 2 3 4 5]

5x2 Array:
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]]

Result:
[ 95 110]
dimension of the array is :  (2,)'''