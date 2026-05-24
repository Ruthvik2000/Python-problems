a=10
print(a)
print(id(a))
#id function is used to get the  address of the variables
#output :9756512
"""
The memoryview() method returns a memory view object of the given object. 
The memoryview object allows Python code to access the internal data of an object that supports the buffer protocol without copying.
The memoryview is one of the binary data types in python
"""
x = memoryview(bytes(a))
print(x)
#outtput:<memory at 0x2b3dacb1ca00>