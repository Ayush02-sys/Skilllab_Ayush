a=20 #its normal variable
b=20,30,40,50 #this is tuple
print(type(a))
print(type(b))

# b=()
# print(type(b))
print(b)

#two ways to declare
t=10,20,30
d=(10,20,30)

print(d)
print(t)

d=tuple(range(2,6))
print(d)

print(d[2])
print(d[0:10])
print(d[0:11:2])
print(d.index(4))



# d[5]=100 #tuple is immutable

e=d*2#it replicates
ad=d+e#it concatenate
print(e)
print(type(e))
print(ad)
print(type(ad))
print(len(e))

#count gives frequency of element in the tuple
print(ad.count(3))

print(ad[::-1])
print(sorted(ad))
print(min(ad),",",max(ad))