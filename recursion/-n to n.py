n = int(input("enter the number:"))
def rec(n):
    print(-n)
    print(n)
    if n==0:
        return
    else:
        rec(n-1)
rec(n)

"""
enter the number:2
-2
2
-1
1
0

"""

n = int(input("enter the number:"))
def rec(n):
    print(-n)
    if n==0:
        return 
    else:
        rec(n-1)
        print(n)
rec(n)

"""
enter the number:2
-2
-1
0
1
2
"""
