def naturaln(n):
    if n<1:
        return
    else:
        naturaln(n-1)
    print(n)
a=int(input("enter a number:"))
print(naturaln(a))

"""
enter a number:5
1
2
3
4
5
None
"""

def naturaln(n):
    print(n)            #here it prints 1
    if n<2:                #and then checks for 1<2 returns -->function ends
        return
    else:
        naturaln(n-1)   #when n=2 it will go with naturaln(1)
a=int(input("enter a number:"))
print(naturaln(a))
"""
enter a number:5
5
4
3
2
1
None
"""