# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result=[]
        todelete=set(to_delete)

        def dfs(root,todelete,result):
            if not root:
                return None
            
            root.left=dfs(root.left,todelete,result)
            root.right=dfs(root.right,todelete,result)

            if root.val in todelete:
                if root.left:
                    result.append(root.left)
                if root.right:
                    result.append(root.right)
                return None
            return root



        dfs(root,todelete,result)
        if not (root.val in todelete):
            result.append(root)
        return result


        