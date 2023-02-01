class Person:
     firstName=""
     lastName=""
     def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
     def printName(self):
        print("Name: ",self.firstName,self.lastName)

x=Person("Akash","Gupta")
x.printName()

class Student(Person):# Student class is child class of Person Class
     def printName(self):
        super().printName()#getting the properties of parent class
        print("Name",self.lastName,self.firstName)
        #self.printName()

x=Student("Abhishek","Kumar")
x.printName()


