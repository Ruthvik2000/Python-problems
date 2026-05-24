"""
Class Variables — Declared inside the class definition (but outside any of the instance methods). 
 Instance Variable — Declared inside the constructor method  of class (the __init__ method).
 """
 
class Car:

    wheels = 4#class variable

    def __init__(self):#constructor method
        self.mil = 10      #mill,com are instance variables
        self.com = "BMW"
c1 = Car()
c2 = Car()
print(c1.mil)
print(c1.com)
c1.mil = 8
Car.wheels = 5
print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)
"""
output:
10                                                                                                                                            
BMW                                                                                                                                           
BMW 8 5                                                                                                                                       
BMW 10 5 
"""