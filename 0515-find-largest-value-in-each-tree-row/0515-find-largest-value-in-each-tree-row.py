# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        deque=collections.deque()
        deque.append(root)
        result=[]
        while deque:
            maxi=float('-inf')
            for i in range(len(deque)):
                root=deque.pop()
                if root:
                    maxi=max(maxi,root.val)
                    if root.left:
                        deque.appendleft(root.left)
                    if root.right:
                        deque.appendleft(root.right)
            result.append(maxi)
        return result
            



        