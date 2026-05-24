#here sorting the dictionary and taking the output into the list
d = {'one':1,'three':3,'five':5,'two':2,'four':4}
a = sorted(d.items(), key=lambda x: x[1])    
print(a) 

"""
[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]
"""


#if we wnat to sort the dict and store the result in the dictionary itself
a={"b": 10, "c": 9, "a": 5}
ans=dict(sorted(a.items(), key=lambda item: item[0]))
print(ans) 

"""
{'a': 5, 'b': 10, 'c': 9}
""" 

d={9:"abc",8:"dfbg",6:"ax"} 
for i in sorted(d.keys())[::-1]:
    print(d[i]) 

"""
abc
dfbg
ax

"""