import csv 

with open("marks.csv","w",newline="") as file:
    writer=csv.writer(file)

    writer.writerow(['name','marks'])

    number_of_students=int(input("Enter the total no. of students: "))
    for i in range(number_of_students):
        name=input("Enter Students Name : ")
        marks=input("Enter the marks obtain : ")
        writer.writerow([name,marks])