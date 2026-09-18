#sentence input 
name = input("Enter List :- ")
#sentence print
print(name)

#convert into lower case
low=name.lower()
print(low)

#split the word
split_sentence=name.split()
print(split_sentence)

#count total words
count=len(split_sentence)
print("Number of words : ",count)

#Find word in the sentence
word=input("Enter the word :")
if word in name:
    print(True)
else:
    print(False)
    