def swap(a,b):
    a=a^b #step1
    b=a^b #step2
    a=a^b #step 3
    print(a,b)
swap(10,11)
"""
output:
11 10
"""
"""
10--->1010
11--->1011

"""
#step 1 a=0001
#step 2 b= 0001 ^ 1011 -->1010 i.e 10
#step 3 a= 0001 ^ 1010 -->1011 i.e 11