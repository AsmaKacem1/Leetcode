# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depestLevel=0
        somme=0
     
        def dfs(root,level):
            nonlocal depestLevel, somme
            if not root:
                return
            if depestLevel==level:
                somme+=root.val
            elif depestLevel<level:
                depestLevel=level
                somme=root.val
            dfs(root.left,level+1) 
            dfs(root.right,level+1)
        dfs(root,0)
        return somme
            
        

       