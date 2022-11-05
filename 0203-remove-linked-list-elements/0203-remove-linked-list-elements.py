# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val==val:
            head=head.next
        delt=head
        while(delt and delt.next):
            if delt.next.val==val:
                delt.next=delt.next.next
            else:
                delt=delt.next
        return head