k=str(input("enter the string:"))
l=k.split()
d={}
for i in l:
    ch=i[0]
    if not ch in d:
        d[ch]=[]#we create keys without duplicate and values as a empty list
    d[ch].append(i)#then after we will append the suitable strings with same starting char into list
print(d)

"""
output:
enter the string:apple orange animal cricket bat ball                                                                                         
{'c': ['cricket'], 'o': ['orange'], 'b': ['bat', 'ball'], 'a': ['apple', 'animal']}     
"""