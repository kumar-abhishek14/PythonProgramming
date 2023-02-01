x=lambda a,b:a+b
y=lambda a,b:a-b
z=lambda a,b:a*b
k=lambda a,b:a/b

a=int(input("Please enter the first number :"))
operator=input("Please enter a operator : ")
b=int(input("Please enter the second number"))
if operator=="+":
    print(x(a,b))
elif operator=="-":
    print(y(a,b))
elif operator=="*":
    print(z(a,b))
else :
    print(k(a,b))
