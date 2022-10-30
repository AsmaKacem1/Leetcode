# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        new_node=head
        while(new_node):
            i+=1
            new_node=new_node.next
        for j in range(i//2):
            head=head.next
        return head
            