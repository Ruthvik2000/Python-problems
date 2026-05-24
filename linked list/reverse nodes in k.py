# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head 
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next 
        if head==None or k==1 or count==1:
            head
        curr=dummy 
        nextnod=dummy
        prev=dummy
        while(count>=k):
            curr=prev.next
            nextnod=curr.next 
            for i in range(1,k+1):
                curr.next=nextnod.next
                nextnod.next=prev.next
                prev.next=nextnod
                nextnod=curr.next
            prev=curr
            count=count-k 
        return dummy.next