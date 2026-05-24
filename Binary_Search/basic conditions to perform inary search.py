#we need to make sure that the list to be sorted at the beggining 
#why we go for binary search than linear search?
"""
The main advantage of using binary search is that it does not scan each element in the list. Instead of scanning each element,
 it performs the searching to the half of the list.
 So, the binary search takes less time to search an element as compared to a linear search.
"""
"""
As linear search scans each element one by one until the element is not found. If the number of elements increases,
 the number of elements to be scanned is also increased.
 We can say that the time taken to search the elements is proportional to the number of elements. 
 Therefore, the worst-case complexity is O(n)
"""
 #step1:intialy the first index is lower bound,last index is upperbound,then  find the mid value of the list using indexes
"""
 step2:
 if the searcing value is equals to the mid value of the list we are searching for ,then the solvation completes
if the searching value is less than the mid value then make that mid value as lower value,
now a new list will be created [lowerbound(firstindex),mid-value(mid_index-1)],now again found the mid  value in the newlist again compare with the searching value
here so many numbers in b/w intial lower,mid value will be skipped.So,we wont compare with all the elements in the list
 if the searching value is greater than the mid value then make that the midvalue as greater value,
 now a new list will be generated [mid-value(mid_index+1),upper bound(lastindex)],again found the mid-value in the new list and compare that with searching value
 therfore do this type of iteration till we found the search-value
2"""
pos=-1#intialy we consider position(or)index of the search value is at -1.so,that no-debugging occurs
def search(list, n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['pos']=mid
            return pos
        else:
            if list[mid] < n:
                l = mid+1;
            else:
                u = mid-1;

list = [4,7,8,12,45,99,102,702,10987,56666]
n =102

if search(list, n):
    print("Found at ",pos)
else:
    print("Not Found")