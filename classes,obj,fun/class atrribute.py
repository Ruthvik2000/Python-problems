class Student:
    count = 0
    def __init__(self):
        Student.count += 1   

std1=Student()
Student.count
#1 
std2 = Student()
Student.count
#2
"""
In the above example, count is an attribute in the Student class. 
Whenever a new object is created, the value of count is incremented by 1.
 You can now access the count attribute after creating the objects, as shown below.
"""