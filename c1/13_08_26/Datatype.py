datatype="Ayush yadav"
print(datatype,"=",type(datatype))
print(datatype[0],
      datatype[1:4],
      datatype[-2],
      datatype[::-1])
print(datatype.upper().replace('A','Z').split(' '))
first_name,second_name=datatype.split(" ")
print(f"First Name is {first_name} and second name is {second_name}.")
datatype=150.55
print(datatype,"=",type(datatype))
datatype=int(datatype)
print(datatype,"=",type(datatype))
datatype=150+55j
print(datatype,'=',type(datatype))
print(datatype.real,
      datatype.imag,
      datatype.conjugate())
a,b=150,0.5
print(a+b,
      a-b,
      a*b,
      round(a**b,2),
      a/b,
      a//b,
      abs(b-a),
      b-a)