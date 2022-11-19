# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L=res=ListNode()
        while (list1 and list2):
            if list1.val<list2.val:
                L.next=list1
                L=list1
                list1=list1.next
            else:
                L.next=list2
                L=list2
                list2=list2.next
        if list1 or list2:
            L.next=list1 if list1 else list2      
        return res.next
        
        
           
      