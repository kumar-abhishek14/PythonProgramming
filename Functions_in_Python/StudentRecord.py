class Student:
    name=""
    section=""
    subject1=0
    subject2=0
    subject3=0
    def __init__(self,name,section,subject1,subject2,subject3):
        self.name=name
        self.section=section
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
    def totalMarks(self):
        return self.subject1+self.subject2+self.subject3
    def printDetails(self):
        print("Name : ",self.name,"section :",self.section)

student1=Student(input("Name "),input("Section "),int(input("Subject1")),int(input("Subject2")),int(input("Subject3")))
student2=Student("Ghanshyam","BCA",50,70,70)
student3=Student("Ravi","BCA",80,40,70)
student4=Student("Rishav","BCA",30,90,70)
student5=Student("Ashish","BCA",30,80,70)
student1.printDetails()
print(student1.totalMarks())
student2.printDetails()
print(student2.totalMarks())
student3.printDetails()
print(student3.totalMarks())
student4.printDetails()
print(student4.totalMarks())
student5.printDetails()
print(student5.totalMarks())