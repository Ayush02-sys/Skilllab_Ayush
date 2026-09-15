number=int(input('Enter the no. to be checked = '))
if number>=2:
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            print("not prime")
            break
    else:
        print("prime number")
else:
    print("not prime")