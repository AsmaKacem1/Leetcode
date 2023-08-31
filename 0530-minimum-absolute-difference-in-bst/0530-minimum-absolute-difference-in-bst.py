# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def getMinimumDifference(self, root):
            def dfs(root,liste):
                if not root:
                    return
                dfs(root.left,liste)
                liste.append(root.val)
                dfs(root.right,liste)
            liste=[]
            dfs(root,liste)
            min_diff=float('inf')
            for i in range(len(liste)-1):
                min_diff=min(min_diff,liste[i+1]-liste[i])
            return min_diff