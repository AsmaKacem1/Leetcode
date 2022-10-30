# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv=None
        while head:
            new_node=head
            head=head.next
            new_node.next=prv
            prv=new_node
            
        return prv
        