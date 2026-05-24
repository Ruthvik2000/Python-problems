def split_and_join(line):
    # write your code here
    x=line.split(" ")
    print(x)
    y="-".join(x)
    print(y)
line=input("enter the string:")
k=split_and_join(line)
print(k)
"""
output:
enter the string:this is a
['this', 'is', 'a']
this-is-a
"""
    