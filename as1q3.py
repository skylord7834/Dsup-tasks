#write a program to input a string and count the number of words in it.
def countWords(s):
    words=s.split()
    return len(words)

string=input("Enter a string: ")
numOfWords=countWords(string)
print("Number of Words is",numOfWords)

'''
output:-
Enter a string: count the words in a string
Number of Words is 6
'''