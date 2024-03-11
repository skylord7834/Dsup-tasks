import numpy as np
array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array2 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 8, 7, 5],
                   [5, 2, 3, 4]])
productArray=np.multiply(array1,array2)
print("The product of 2 4x4 array is:")
print(productArray)



'''
out:-
The product of 2 4x4 array is:
[[ 1  4  9 16]
 [25 36 49 64]
 [81 80 77 60]
 [65 28 45 64]]
 '''