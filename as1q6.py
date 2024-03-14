#  Write a Python program to interchange first and last elements in a list
def interchange(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
list1=[1,2,3,4,5,6]
print("original list =",list1)
newList=interchange(list1)
print("swapped list = ",newList)

'''
output:-
original list = [1, 2, 3, 4, 5, 6]
swapped list =  [6, 2, 3, 4, 5, 1]
'''


