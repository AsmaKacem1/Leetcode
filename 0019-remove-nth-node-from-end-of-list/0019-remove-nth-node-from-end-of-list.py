# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i,j=0,0
        curr=head
        while curr:
            i+=1
            curr=curr.next
        if (n==i):
            head=head.next
            return head
        cur=head
        while j<(i-n-1):
            j+=1
            cur=cur.next
           
        cur.next=cur.next.next
        return head
        