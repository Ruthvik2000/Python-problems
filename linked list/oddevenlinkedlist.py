# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        temp1=head
        c = 1
        while temp1.next!=None:
            temp1= temp1.next
            c += 1
        #now the temp1 will points to the 5
        i=0
        prev=head
        temp=head
        while i<c:
            if i % 2 != 0:
                temp1.next=ListNode(temp.val)
                temp1=temp1.next
                prev.next = prev.next.next
                prev= prev.next
            temp=temp.next 

"""
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
"""