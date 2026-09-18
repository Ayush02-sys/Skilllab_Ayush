#WAP to print different vowels present in the given word
words=input("Enter the word/sentence: ").lower()
letters=set(words)
vowels={'a','e','i','o','u',}

found=letters.intersection(vowels)
print("the vowel found in the given input is/are : ",found)
