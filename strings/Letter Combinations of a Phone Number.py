digits=str(input("enter the digit in between 2 to 9:"))
phno={
    "2":'abc',
    "3":'def',
    "4":'ghi',
    "5":'jkl',
    "6":'mno',
    "7":'pqrs',
    "8":'tuv',
    "9":'wxyz'            
}
if digits =="":
    print([])
numbers=list(phno[digits[0]])#making the list for the 1'st digit of the digits string from phno dictinory
for i in digits[1:]:
    numbers=[m+n for m in numbers for n in list(phno[i])]#its like a double for loop
print(numbers)
"""
output:

enter the digit in between 2 to 9:23                                                                                                          
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']   
"""