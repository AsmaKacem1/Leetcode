# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True


        pointer=head
        prev=None
        while pointer:
            copy = ListNode(pointer.val)
            copy.next = prev
            prev = copy
            
            pointer = pointer.next
            



        while head and prev:
            if(head.val!=prev.val):
                return False
            else:
                prev=prev.next
                head=head.next
        return True
        