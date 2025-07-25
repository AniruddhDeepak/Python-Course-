Students={"Alice":"85","Mick":"45","Nick":"95"}
student_name=input("Enter the student's name : ")
if student_name in Students:
   print(f"{student_name}'s marks : ",Students[student_name])
else:
    print("Student not found")



