# a={101:'Ayush',
#    102:'70',
#    103:'BCA',
#    104:'skill lab'}# dictionary is a key-value pair data structure
# print(a)
# print(type(a))
# print(a[102])

na={}
e=int(input("Give the number of students"))
i=1
while i<=e:
    name=input("student name : ")
    marks=int(input("Enter the marks obtain : "))
    na[name]=marks
    i+=1
print("Name of the student","\t","Marks")
for x in na:
    print("\t",x,"\t\t",na[x])
