# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deque=collections.deque()
        deque.append(root)
        result=0
        while deque:
            for i in range(len(deque)):
                node=deque.popleft()
                if node.left:
                    deque.append(node.left)
                result+=node.val
                if node.right:
                    deque.append(node.right)
            if len(deque)!=0:
                result=0
        return result 