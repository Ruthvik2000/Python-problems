"""
if the method which we want to use in other classes is classmethod method then we need to use an object to get the classicmethod 
of other class
"""
class A():
    def methoda(self):
        print("Class A method")
        return "2"
    def methodc(self):
        y=self.methoda()#as methoda is from the same class and its a instance method so we will use self
        print("methoda of same class A was called {}".format(y))
        obj=B()#we can use the same object name given to A class (or) we can also take other name for object
        x=obj.methodb()#its like classnameofthemethodwhichwewant to take.method()
        print("methodb in class B was called {}".format(x))#if want to get the return of the method which we use then use format
       
class B():
    school='KKR'
    @classmethod
    def methodb(cls):
        return cls.school
obj=A()
obj.methodc()