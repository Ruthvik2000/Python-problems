"""
Nonlocal variables are used in nested functions whose local scope is not defined.
This means that the variable can be neither in the local nor the global scope.
Let's see an example of how a nonlocal variable is used in Python.
We use nonlocal keywords to create nonlocal variables.
"""

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

"""
inner: nonlocal
outer: nonlocal
"""

"""
In the above code, there is a nested inner() function.
 We use nonlocal keywords to create a nonlocal variable. 
The inner() function is defined in the scope of another function outer().
"""