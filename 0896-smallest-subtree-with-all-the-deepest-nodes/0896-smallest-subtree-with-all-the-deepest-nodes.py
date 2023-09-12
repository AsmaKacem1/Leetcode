# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthNode(self,node,depth):
        if not node:
            return depth;
        return max(self.depthNode(node.left,depth+1),self.depthNode(node.right,depth+1))

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        if not root.left and not root.right:
            return root
        depthLeft=self.depthNode(root.left,0) if root.left else 0
        depthRight=self.depthNode(root.right,0) if root.right else 0

        if depthLeft==depthRight:
            return root
        elif depthLeft>depthRight:
            return self.subtreeWithAllDeepest(root.left)
        else: 
            return self.subtreeWithAllDeepest(root.right)

    


        
        
         

