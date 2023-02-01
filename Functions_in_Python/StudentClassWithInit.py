class Student:
    name=""
    course=""
    subjects=""
    def __init__(self,name,course,subjects):
        self.name=name
        self.course=course
        self.subjects=subjects
    def printDetails(self):
        print("Name: ",self.name,"course :",self.course,"subjects",self.subjects)
        
ghanshyam=Student("Ghanshyam","BCA","Java")
akash=Student("Akash","B.sc","Chemistry")
abhi=Student(input(),input(),input())
ghanshyam.printDetails()
akash.printDetails()
abhi.printDetails()