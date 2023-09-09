# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]

        def dfs(root,string):
            nonlocal result
            if not root:
                return 
            string+=str(root.val)+"->"
            dfs(root.left,string)
            dfs(root.right,string)
            if not root.left and not root.right:
                result.append(string[:-2])
        dfs(root,"")
        return result
        
        