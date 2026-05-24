k=input("enter the string:")
l=k.split()
d={}
for i in l:
    if not i in d:
        d[i]=0#making the value for all the keys as zero and its like creating the keys and intializing there values to zero
    d[i]=d[i]+1#now the for loop executes for i in l increments by 1(its like in this stepthe values will be provided correctly)
print(d)
"""
its a function of counting a sub string in the input string k
output:

entert the string:hi hello hello world how r u                                                                                                
{'u': 1, 'hello': 2, 'hi': 1, 'world': 1, 'r': 1, 'how': 1}   
"""