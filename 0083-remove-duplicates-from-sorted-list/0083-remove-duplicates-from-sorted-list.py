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
        node2=head.next
        while node2:
            if (node1.val==node2.val):
                node2=node2.next
                node1.next=node2
            else:
                node1=node1.next
                node2=node2.next
        return head
                
                
        