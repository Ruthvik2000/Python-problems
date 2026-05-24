
nums = [10,16,18,21,26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")

"""
output:
10
not found
beacause for the remaining number the if statement is not working
if the else statement in the for loop then it will print not found four times
but if the else loop is in the out of for loop it will show result only ones even though the eslse executes 4 times

nums = [10,16,18,21,26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
        print("not found")

then output will be:
  5
  not found
  not found
  not found
  not found
  4 times it will repeat 
"""