a=range(5)
b=range(1,10)
c=range(1,10,2)

for x in a:
    print(x, end=" ")
print(" ")

for x in b:
    print(x, end=" ")
print(" ")

for x in c:
    print(x, end=" ")
print("\n")

for i in range(1,16,3):
    print(f"{i} = hello world")
print("\n")

for i in range(1,16,3):
    print(f"{i}", end=" ")
print("\n")

x=int(input("enter no."))
for i in range(1,11):
    print(f"{x} * {i} = {i*x}")
print("\n")

for i in range(x):
    if i<=10:
        print(f"{x} * {i} = {i*x}")
    else:
        break