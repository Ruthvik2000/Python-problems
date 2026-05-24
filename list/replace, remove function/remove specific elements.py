x=['a','b','c','d','e','f','g','h']
print(x)
print(pop())#delets the last element
print(pop(4))#delets an element of specific  index
print(del x[2:6])#delets the elements of specific range
print(del x[1])#we can also an element at specific index using del kyword
print(x.clear())

y=[1,2,3,4,5,6,7,8,9]#if we ant to delete the alterntive elemts and print this in reverse
print(del y[::1])#or simmply by printing the print(x[::2]) it will print the alternative y automaticaly deleting the mis values
prinrt(y[::-1])#will print the list in reverse 
