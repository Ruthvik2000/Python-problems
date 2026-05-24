h=[int(a) for a in input("enter the numbers").split()]
print(h)
d={}
for i in range(len(h)):
    if not h[i] in d:
        d[h[i]]=[]
    d[h[i]].append(i)
print(d)
"""
enter the numbers1 2 3 3
[1, 2, 3, 3]
{1: [0], 2: [1], 3: [2, 3]}
"""