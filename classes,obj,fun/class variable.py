"""
A Python class variable is shared by all object instances of a class. 
Class variables are declared when a class is being constructed. 
They are not defined inside any methods of a class.
Because a class variable is shared by instances of a class, the Python class owns the variable. 
As a result, all instances of the class will be able to access that variable. 
Class variables are shared by all instances that access the class.
"""

class Espresso:
	menu_type = "Drink"

espresso_order = Espresso()
espresso_order.menu_type = "Coffee"
print(espresso_order.menu_type)
a=Espresso()
print(a.menu_type)

"""
output:
Coffee
Drink

"""