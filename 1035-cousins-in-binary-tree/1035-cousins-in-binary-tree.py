# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        deque=collections.deque()
        deque.append(root)
        while deque:
            count=0
            for i in range(len(deque)):
                node=deque.popleft()
                if node.left:
                    deque.append(node.left)
                    if x==node.left.val or y==node.left.val:
                        count+=1
                if node.right:
                    deque.append(node.right)
                    if x==node.right.val or y==node.right.val:
                        count+=1
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False 
            if count==2 :
                return True
        return False
            


        