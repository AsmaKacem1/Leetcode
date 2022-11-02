# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summ=0
        def inorder(root):
            if root:
                if root.val>low:
                    inorder(root.left)
                if low<=root.val<=high:
                    self.summ+=root.val
                if root.val<high:
                    inorder(root.right)
        inorder(root)
        return(self.summ)
            
        