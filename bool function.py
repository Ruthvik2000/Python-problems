#It returns True if the parameter or value passed is True.
#It returns False if the parameter or value passed is False.
#antey 0 ledha empty string leydha array vuntey "TRUE" return chestadi

"""
If a False value is passed.
If None is passed.
If an empty sequence is passed, such as (), [], ”, etc
If Zero is passed in any numeric type, such as 0, 0.0 etc
If an empty mapping is passed, such as {}.
If Objects of Classes having __bool__() or __len()__ method, returning 0 or False
"""

x = 5
y = 10
print(bool(x==y))
# Returns False as x is None

x = None
print(bool(x))
# Returns False as x is an empty sequence

x = ()
print(bool(x))
# Returns False as x is an empty mapping

x = {}
print(bool(x))
# Returns False as x is 0

x = 0.0
print(bool(x))
# Returns True as x is a non empty string

x = 'GeeksforGeeks'
print(bool(x))
#returns True

"""
output:
False
False
False
False
False
True

"""