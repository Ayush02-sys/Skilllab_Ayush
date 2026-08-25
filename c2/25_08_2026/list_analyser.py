marks=eval(input("Enter the marks of atleast 10 student = "))
total_marks=0
average_marks=0
highest=0
lowest=101
pass_count=0
fail_count=0
if len(marks)<10:
    print('Not enough marks')
else:
    for mark in marks:
        total_marks+=mark
        if mark>highest:
            highest=mark
        elif mark<lowest:
            lowest=mark

        if mark>=40:
            pass_count+=1
        else:
            fail_count+=1

    average_marks=total_marks/len(marks)
    print("="*30,'\n\tMarks Analyser')
    print('='*30)
    print('\nTotal marks = ',total_marks,'\nAverage marks = ',average_marks,'\nHighest marks = ',highest,'\nLowest marks = ',lowest,'\nNo. of Students passed = ',pass_count,'\nNo. of Students failed = ',fail_count)
    print("="*30)