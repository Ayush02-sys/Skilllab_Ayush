# #understanding set
# set1={'name','ayush','class','bca','lab','skill_lab'}
# print(set1)
# print(type(set1).__name__)
# a=set(set1)
# print(a)
# print(type(a).__name__)
# print("the primary set element is : ",a)
# n=input("enter the name to be added: ")
# a.add(n)
# print("the new set is :",a)


# #updating set element

# h={10,15,20,25,30,35,40}
# print(h)
# a=[12.5,17.5,22.5,27.5]
# h.update(a[:2])
# print('after updation : ',h)

# #pop() operation on set

# j={40,50,78,45,"ayush"}
# print("element of j : ",j)
# print(j.pop())
# print("element of j after pop operation : ",j)

# #remove() operation on set 

# k={10,45,"ayush",98,45,67}
# print("Element of k : ",k)
# k.remove("ayush")
# print("Element of K after remove operation :- ",k)

#union (|) of set

u={10,20,30,40,50,60}
print("element of u :",u)
y={15,25,35,45,55}
print("element of y :",y)
print("element after union : ",u|y)

#finding element using membership operator

t=set("this is the data analyst class ")
print("Element of t : ",t)
print('t' in t)
print('o' not in t)
