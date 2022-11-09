# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        L=[]
        if root==None:
            return L
        def inorder(root):
            if root:
                if root.val!=None:
                    L.append(root.val)
                inorder(root.left)
                
                inorder(root.right)
        inorder(root)
        return L
        