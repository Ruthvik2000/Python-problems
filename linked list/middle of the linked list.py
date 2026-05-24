# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        curr=head
        count=0
        while(curr):
            count+=1
            curr=curr.next
        mid=count//2
        curr=head
        for i in range(mid):
            curr=curr.next
        return curr
"""
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""
"""
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

#other way
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """         
        s=head                   # s is the slower pointer
        f=head                   # f is the fast poiter
        while f and f.next:
            s=s.next
            f=f.next.next
        return s
        