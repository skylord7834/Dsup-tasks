# write a program to input a string and remove the duplicate words
def removeDuplicate(s):
    word=s.split()
    uniqueWord=[]
    for i in word:
        if i not in uniqueWord:
            uniqueWord.append(i)
    
    return " ".join(uniqueWord)

sentence=input("Enter a sentence: ")
newSentence=removeDuplicate(sentence)
print(newSentence)



'''
output:-
Enter a sentence: this this is is a a sentence
this is a sentence
'''