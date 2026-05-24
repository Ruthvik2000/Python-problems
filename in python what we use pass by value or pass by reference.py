def update(x):
    print(id(x))
     x = 8
     print(id(x))
      print("x ", x)
a = 10
print(id(a))
update(a)
print("a ", a)
"""
The output will be:
id of a 
id  of x=id od a 
as we changing the value  of x in the update function it wont effect the address and value of a ,a=8 value will be
stored in one address and a=10 value will bw stored n other address
"""
"""
output:
1175862(address of a )
1175862(address of a before intiation of a=8)
1189626(address of a after a=8)
8
10
"""
"""
Generally some  languages handle function arguments as references to existing variables, 
which is known as pass by reference. 
Other languages handle them as independent values, an approach known as pass by value.
"""
"""
Python has a  peculiar way of handling function arguments.
Python’s argument passing model is neither “Pass by Value” nor “Pass by Reference” but it is 
“Pass by Object Reference”.
"""