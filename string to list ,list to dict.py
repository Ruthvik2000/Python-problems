alp="abcdefghijklmnopqrstuvwxyz"
alp=list(alp)
b=[]
d={}
for i in range(len(alp)):
    b.append(i+1)
for i in range(len(alp)):
    d[alp[i]]=b[i]
print(alp)
print(b)
print(d)


"""
output:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']            
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]                                               
{'l': 12, 'q': 17, 'h': 8, 'd': 4, 't': 20, 'b': 2, 'n': 14, 'a': 1, 's': 19, 'x': 24, 'z': 26, 'j': 10, 'r': 18, 'w': 23, 'o': 15, 'e': 5, 'u
': 21, 'i': 9, 'y': 25, 'm': 13, 'f': 6, 'k': 11, 'c': 3, 'v': 22, 'p': 16, 'g': 7}

"""