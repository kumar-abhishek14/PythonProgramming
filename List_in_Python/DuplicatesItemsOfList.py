myList=["Abhi","Apple","Orange","Apple"]
print("List before Removing duplicates",myList)
i=0
while i<len(myList):
      j=i+1
      while j<len(myList):
        if myList[i]==myList[j]:
           myList.remove(myList[j])
        j=j+1
      i=i+1
print("List after removing duplictes",myList)
