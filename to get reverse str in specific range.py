b = "Hello, World!"
x=b[-5:0:-1]
print(x)
#output:oW ,olle
print(x[::-1])
#output:ello, Wo
print(b[-5:-1])
#output:orld
"""
we cant get the results for the following statements
"""
print(b[-5:-1:-1])
print(b[1:5:-1])
"""
we cant get the results for the upper two statemnets for that
first we need to store 
y=b[-5:-1]
z=b[1:5]
and then we eed to reverse them like print(y[::-1]) and print(z[::-1])
"""