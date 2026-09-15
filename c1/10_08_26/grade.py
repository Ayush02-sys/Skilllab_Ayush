import csv

with open('marks.csv', 'r') as infile:
    reader = csv.reader(infile)
    next(reader) 

    with open('grade.csv', 'w', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Name", "Grade"])  

        for row in reader:
            name = row[0]
            marks = int(row[1])

            if marks > 100 or marks < 0:
                Grade = "error"
            elif marks >= 90:
                Grade = "A+"
            elif marks >= 80:
                Grade = "A"
            elif marks >= 70:
                Grade = "B"
            elif marks >= 60:
                Grade = "C"
            elif marks >= 50:
                Grade = "D"
            else:
                Grade = "F"

            print(name,Grade)
            writer.writerow([name, Grade])
