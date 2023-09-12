# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthNode(self,node,depth):
        if not node:
            return depth
        return max(self.depthNode(node.left,depth+1),self.depthNode(node.right,depth+1))
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.depthNode(root.left,0)-self.depthNode(root.right,0))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

