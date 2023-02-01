def func(a):
    return lambda x:x*a

x=func(5)#lambda x:x*5

print(x(2))
print(x(3))
print(x(4))
k=int(input())
print(x(int(input())))