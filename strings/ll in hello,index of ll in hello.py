haystack=str(input("enter the first string:"))
needle=str(input("enter the second string:"))
if not haystack and not needle:
    print("0")
if needle in haystack:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            print(i)
else:
    print("-1")

"""
output:
enter the first string:hello                                                                                                                  
enter the second string:ll                                                                                                                    
2                                                                                                                                             
"""
"""
simply:
print(haystack.index(needle))
"""
"""
another method is using find function
prinT(haystack.find(needle))
"""