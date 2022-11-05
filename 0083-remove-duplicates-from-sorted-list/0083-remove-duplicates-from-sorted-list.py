# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        node1=head
        while node1.next:
            if (node1.val==node1.next.val):
                node1.next=node1.next.next
            else:
                node1=node1.next
        return head
                
                
        