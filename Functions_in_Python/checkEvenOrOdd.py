def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
x=int(input("Please enter a number"))
print("Factorial of number ",x," is ",factorial(x))
