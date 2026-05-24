"""
In Python, a variable declared outside of the function or in global scope is known as
a global variable. 
This means that a global variable can be accessed inside or outside of the function.
To use this variable inside a function you need to use "global" keyword
"""
"""
A variable declared inside the function's body or in the local scope is known as 
a local variable.
we declare a variable inside the function to create a local variable.

"""
x = 5

def foo():
    global x
    print(x)
    x= 10
    print(" x:", x)
    y=20
    print(y)


foo()
print("global x:", x)

"""
5
 x: 10
20
global x: 10
"""