class computer:
    def __init__(self):
        print("this is ruthvik")
    def config(self):
        print("config function")
com1=computer()
com2=computer()
com1.config()
com2.config()
"""
output:
this is ruthvik #com1 execution
config function
this is ruthvik #com2 execution
config function
"""
"""
even though we are not calling init fun it will execute automatically at the run time
"""
