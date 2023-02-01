def removingDuplicates(myList):
    myList2=[]
    for x in myList:
        if x not in myList2:
            myList2.append(x)
    
    for z in myList2:
        print(z,end=" ")

a=[4,6,7,9,3,6]
removingDuplicates(a)