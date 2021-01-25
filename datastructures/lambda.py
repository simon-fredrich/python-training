#!/usr/bin/python3

x = lambda a : a*10

print(x(10))

x = lambda a, b : a**b

print(x(2, 2))

x = lambda a, b, c : a + b * c

print(x(2, 5, 2))

# A function which can multiply by any number.
def myfunc(n):
    return lambda a : a*n

# The function y multiplies by 2 
y = myfunc(2)
print(y(13))

# The function z multiplies by 8
z = myfunc(8)
print(z(6))