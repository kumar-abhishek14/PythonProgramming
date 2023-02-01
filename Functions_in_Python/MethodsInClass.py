class Laptop:
    ramSize=""
    def isLaptopWorking(self):
        print(self.ramSize)
    def __init__(self,size):
        self.ramSize=size

laptop=Laptop(int(input("please enter the size")))

laptop.isLaptopWorking()