"""
if the method which we want to use in other classes is instance method then we need to use an object to get the classicmethod 
of other class
"""
class A():
    def __init__(self):
        pass
    def methoda(self):
        print("Class A method")
        return "2"
    def methodc(self):
        obj1=B()#we can use the same object name given to A class (or) we can also take other name for object
        x=obj1.methodb()#its like classnameofthemethodwhichwewant to take.method()
        print("methodb in class B was called {}".format(x))#if want to get the return of the method which we use then use format
        y=self.methoda()#as methoda is from the same class and its a instance method so we will use self
        print("methoda of same class A was called {}".format(y))
class B():
    def __init__(self):
        pass
    def methodb(self):
        print("class B method")
        return "3"
obj=A()
obj.methodc()