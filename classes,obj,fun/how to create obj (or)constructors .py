class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()#com1 is obj
com2 = Computer()#com2 is obj

Computer.config(com1)
Computer.config(com2)
#generally we use the below line to get a fuc in a class
com1.config()#fun config of class computer takes obj com1 as an argument and executes the config function
com2.config()
"""
So,to get the user defined fun(or)method , variables we use objectes.
that's why we use to say classes are the clue prints of the objects.
"""
"""
to access the variables(or) attributes ,methods of the class through objects we use the keyword self
"""