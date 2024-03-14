#  Write a Python program to find the common elements between two lists. 
list1=[1,2,3,4,5,6,7]
list2=[4,5,6,7,8,9,0]
commonElements=[]
for item in list1:
    if item in list2:
        commonElements.append(item)
print("common elements: ",commonElements)

'''
output:-
common elements:  [4, 5, 6, 7]
'''