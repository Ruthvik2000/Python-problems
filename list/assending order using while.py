dl= [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
while dl:
    mini= dl[0]  # arbitrary number in list 
    for x in dl:
        if x < mini:
            mini = x
    new_list.append(mini)#every min value will be append to new_list as per for loop iteration
    dl.remove(mini)#because while loop will complete only when objects in data_list completes
print(new_list)
"""
 generally we use to 
 dl= [-5, -23, 5, 0, 23, -6, 23, 67]
d1.sort()#prints in assending order
 print(d1)
"""