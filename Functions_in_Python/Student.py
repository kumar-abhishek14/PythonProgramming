class Student:
    name=""
    course=""
    subjects=[]
ghanshyam=Student()
print("Please enter the details of Student 1 :")
ghanshyam.name=input("Please enter the name")
ghanshyam.course=input("please enter the course ")
number=int(input("Please enter the number of Subject"))
for x in range(1,number+1):
    ghanshyam.subjects.append(input("Please enter a subject"))
        

print("Name",ghanshyam.name)
print("course",ghanshyam.course)
print("subjects",ghanshyam.subjects)



    