"""
generally we can implement stack using two types:list and modules
list operation simply contains append and pop function to add,remove the eements 
modules will be like collections and queue
collections module contains class deque,where deque contains functions like push and pop same as like in list
queue module contain class LifoQueue whoch contains put and get method to add,remove the elements from stack
"""
stack=[]#implementing stack using list
stack.append(10)
stack.append(20)
stack.append(30)
print(stack[-1])#last element which entered i.e top most element
print(stack[0])#bottom most elements
 
