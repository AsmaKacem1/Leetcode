# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count,result=0,0
        def dfs(root,maxi):
            nonlocal count,result
            if not root:
                return 
            if root.val>=maxi:
                maxi=root.val
                count+=1
            dfs(root.left,maxi)
            dfs(root.right,maxi)
            result+=count
            count=0
        dfs(root,root.val)
        return result
        