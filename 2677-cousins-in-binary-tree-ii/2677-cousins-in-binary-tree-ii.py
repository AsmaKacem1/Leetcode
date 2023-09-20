# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_somme=defaultdict(int)
        def levelSomme(root,depth):
            if not root:
                return
            level_somme[depth]+=root.val
            levelSomme(root.left,depth+1)
            levelSomme(root.right,depth+1)

        def dfs(root,depth,sib):
            if not root:
                return
            root.val=level_somme[depth]-root.val-sib
            left_val=root.left.val if root.left else 0
            right_val=root.right.val if root.right else 0

            dfs(root.left,depth+1,right_val)
            dfs(root.right,depth+1,left_val)

        levelSomme(root,0)
        dfs(root,0,0)
        return root


        