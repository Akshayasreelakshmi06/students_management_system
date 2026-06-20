students=[]
for i in range(3):
    name=input("Enter student name:")
    marks=[]
    for j in range(3):
        marks=int(input("Enter the mark:"))
        marks.append(mark)
    total=sum(marks)
    avg=total/len(marks)
    if avg>=50:
        result="pass"
    else:
        result="fail"
    
    
    student={
        "name":name,
        "marks":marks,
        "total":total,
        "avg":avg,
        "result":result
        }
    students.append(student)
print("\n----STUDENT REPORT----")
for s in students:
    print("\nName:",s["name"])
    print("\nmarks:",s["marks"])
    print("\ntotal:",s["total"])
    print("\navg:",s["avg"])
    print("\nresult:",s["result"])
    
