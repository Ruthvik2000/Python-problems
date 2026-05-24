#if the method which we want to use in other classes is static method then we can normally by using a variable
class A():
    def __init__(self):
        pass
    def methoda(self):
        print("Class A method")
        return "2"
    def methodc(self):
        x=B.methodb()#its like classnameofthemethodwhichwewant to take.method()
        print("methodb in class B was called {}".format(x))#if want to get the return of the method which we use then use format
        y=self.methoda()#as methoda is from the same class and its a instance method so we will use self
        print("methoda of same class A was called {}".format(y))
class B():
    def __init__(self):
        pass
    @staticmethod 
    def methodb():
        print("class B method")
        return "3"
obj=A()
obj.methodc()