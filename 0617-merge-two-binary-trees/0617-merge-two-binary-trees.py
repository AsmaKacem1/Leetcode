# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and root2:
            return root2
        elif not root2 and root1:
            return root1
        elif not root1 and not root2:
            return 

        val1=root1.val if root1 else 0
        val2=root2.val if root1 else 0
        new_root=TreeNode(val1+val2)
        new_root.left=self.mergeTrees(root1.left,root2.left)
        new_root.right=self.mergeTrees(root1.right,root2.right)

        return new_root



    
        