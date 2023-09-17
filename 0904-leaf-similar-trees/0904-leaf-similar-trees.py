# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,liste):
            if not root:
                return 
            dfs(root.left,liste)
            if not root.left and not root.right:
                liste.append(root.val)
            dfs(root.right,liste)
            return liste
        liste1=[]
        liste2=[]
        dfs(root1,liste1)
        dfs(root2,liste2)
        return liste1==liste2
          