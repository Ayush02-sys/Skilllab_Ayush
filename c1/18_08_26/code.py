#WAP to take tuple of numbers from user and print its sum and avg?
#eval is evaluate function that evaluate the input in python , whether its str int list tuple etc
t=eval(input("enter multiple numbers seprated by commas : "))
# l=len(t)
sum=0
for x in t:
    sum+=x
avg=sum/len(t)
print("The sum of numbers in tuple is : ",sum,"\nThe average of numbers in tuple is : ",avg)