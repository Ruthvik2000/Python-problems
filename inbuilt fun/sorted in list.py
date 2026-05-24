l=["dfg","hjks","rhjtd"]
l=sorted(l,key=len)
print(l) 

"""
['dfg', 'hjks', 'rhjtd']
""" 

a= [("HTML", 15, 'M01'), ("JavaScript", 10, 'M03'), ("Bootstrap", 5, 'M02')]
# Sort the list based on the second item of the tuple
sorted_list1 = sorted(a,key=lambda x: x[1]) 
print(sorted_list1) 
 
"""
[('Bootstrap', 5, 'M02'), ('JavaScript', 10, 'M03'), ('HTML', 15, 'M01')] 
""" 

lst = ['id01', 'id10', 'id02', 'id12', 'id03', 'id13']
lst_sorted = sorted(lst, key=lambda x: int(x[2:]))
print(lst_sorted) 

"""
['id01', 'id02', 'id03', 'id10', 'id12', 'id13']

""" 

