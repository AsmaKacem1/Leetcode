# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def binary_Decimal(n):
            return int(n,2)
            
        def dfs(root,somme):
            if not root:
                return 0
            somme=somme*10+root.val

            if not root.left and not root.right:
                return binary_Decimal(str(somme))
            
            return dfs(root.left,somme) + dfs(root.right,somme)

        return dfs(root,0)
        