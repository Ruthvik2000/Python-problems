class Student:
    school = 'KKR'#class variable or static variable

    def __init__(self,m1,m2,m3):#m1,m2,m3 are instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):#instance method where we need to use"self" as a first parameter to pass as a object
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):#to use the class variables we need to use "cls" as a parametere and also the decorater @classmethod
        return cls.school
                    """
                    if we do not want to need use a class or instance variables (or) calss methods  or instance  methods 
                    then we will use  static method.
                    it like using irrelavant fun like factorial fun using in the present class student
                    """
    @staticmethod 
    def info():
        print("This is Student class.. in abc molude")

s1 = Student(34,47,32)
s2 = Student(89,32,12)

print(s1.avg())
print(Student.getSchool())#we can also write as s1.info() because s1  was created as an object to the class Student
Student.info()#as we cant pass a object to run the info fun ,we need to call the static fun using class name


"""
we can call instance fun,class fun using objects because they contain self,cls as there parameter
But as there wont be an parameter for the static method we need to call the static fun using class namae and dot operator
"""