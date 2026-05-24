#when to use a lamda function
"""
1.If we have only one expression to complete the function like square of a single number:a*a,etcc__
2.if there is no further use of a function in other modules or in ant other function 
3.when we dont want to define the name of a function

Then we will use lamda function
"""
#TEXT BOOK DEFINATION
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
"""
#for example Create a lambda function that takes one parameter (a) and returns it.

x=lambda a:a

#Summarize argument a, b, and c and return the result:
 x=lambda a,b,c:a+b+c
 print(x(4,5,6))
#15

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

"""
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
"""
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#22:n is 2 and a=11