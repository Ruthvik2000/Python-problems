class Computer:
    def __init__(self,cpu,ram):#instance variables
        #__init__ method used to allow the class to create(or)to intialize the variables of the class
        self.cpu = cpu#user defined variable
        self.ram = ram#user defined
        self.name ="window"#normal variabe
    def config(self):
        print("Config is ",self.cpu, self.ram)
    def fgh(self,x):
        self.x=x
        print(x)
com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)
com1.config()
com2.config()
com1.fgh(20)
print(com1.name)#as we need to print the variable we cant print as a function with print funcction 
"""
output:
Config is  i5 16
Config is  Ryzen 3 8
20
window
"""