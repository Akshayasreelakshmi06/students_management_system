students=[]
def add_student():
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    student={
        "name":name,
        "marks":marks
        }
    students.append(student)
    print("student added successfully")
def display():
    for student in students:
        print("Name:",student["name"])
        print("marks:",student["marks"])
        print()
def find_topper():
    if len(students)==0:
        print("no students found")
        return
    topper=students[0]
    for student in students:
        if student["marks"]>topper["marks"]:
            topper=student
    print("topper:",topper["name"])
    print("marks:",topper["marks"])
def avg_marks():
    if len(students)==0:
        print("no students found")
        return
    total=0
    for student in students:
        total+=student["marks"]
    avg=total/len(students)
    print("average marks:",avg)    
                                   
while True:
    print("\n1.Add student")
    print("\n2.Display")
    print("\n3.find topper")
    print("\n4.average marks")
    print("\n5.Exit")

    choice=input("Enter ur choice:")

    if choice=="1":
        add_student()
    elif choice=="2":
        display()
    elif choice=="3":
       find_topper()
    elif choice=="4":
        avg_marks()
    elif choice=="5":
         print("Thanks!")
         break
        
    else:
        print("Invalid choice")
          
