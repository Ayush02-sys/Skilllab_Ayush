# python revision 

# deduplicate the list 
student_ids = [101, 102, 101, 103, 102, 104]
#core logic set store unique values 
#so convert it into set then into list
student=list(set(student_ids))
print(student)
