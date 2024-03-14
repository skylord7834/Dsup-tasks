# 2 Write a program to input a string and check whether it is palindrome or not
def checkPalindrome(s):
    newStr=s.lower()
    # print(newStr)
    return newStr==newStr[::-1]
    
    
string=input("Enter a string: ")
if checkPalindrome(string):
    print('string entered is pallindrome')
else:
    print("entered string is not pallindrome")


'''
output:-
Enter a string: asdsa
string entered is pallindrome

output:-
Enter a string: asdfg
entered string is not pallindrome
'''