"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return None
        leftMost=root
        while leftMost and leftMost.left:
            current=leftMost
            while current:
                current.left.next=current.right
                if current.next:
                    current.right.next = current.next.left 
                current=current.next
            leftMost=leftMost.left
        return root

      