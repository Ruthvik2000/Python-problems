class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, head):
        prev=None
        while head:
            curr=head
            head=head.next 
            curr.next=prev 
            prev=curr
        return prev
"""
Input: 1->2->3->4->5->NULL
output: 5->4->3->2->1->NULL
"""

#method-2:
class Solution:
    def reverseList(self, A):      #same process but taking a pointer curr to traverse
        prev=None
        curr=A
        while(curr):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev 

#method-3:contunious reversing in a range of k 
#like k rverse linked list and alternate k reverse (see in interview bit)