class Account:
    accountNo=0
    accountName=""
    #intializing the class members
    def __init__(self,accountNo,accountName):
        self.accountNo=accountNo
        self.accountName=accountName

acc1=Account(12345,"Test")
acc2=Account(12346,"Test2") 
print(acc1.accountName)
print(acc1.accountNo)
print(acc2.accountName)
print(acc2.accountNo)