# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        deque=collections.deque()
        deque.append(root)
        while deque:
            i=0
            for i in range(len(deque)):
                i+=1
                node=deque.popleft()
                if node.left:
                    deque.append(node.left)
                if i==1:
                    result=node.val
                if node.right:
                    deque.append(node.right)
        return result
        