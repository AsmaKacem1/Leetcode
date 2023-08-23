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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
           return root
        deque=collections.deque()
        deque.append(root)
        while deque:
            prev=None
            for i in range (len(deque)):
                node=deque.popleft()
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

        return root