num1=str(input("enter the first charcheter:"))
num2=str(input("enter the second charcheter:"))
s1 = 0
for i in num1:
    s1 = s1*10 + (ord(i) - 48)  
"""
ord() function returns the number representing the unicode code of a specified character. 
and the reason we deducted 48 beacuse ascii value of 2 is 50 so if we won't deduct 48 which is the ascii value of 0 
it will return 50 and yes you may try this with any no.
"""
# similary we will do for s2    
s2 = 0
for i in num2:
    s2 = s2*10 + (ord(i) - 48)   
# and just return the value      
print(str(s1 * s2))  
        