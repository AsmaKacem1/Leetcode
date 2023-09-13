# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        firstMin = root.val
        secondMin = float('inf')
        result = float('inf')
        deque = collections.deque()
        deque.append(root)

        while deque:
            node = deque.popleft()

            if node.val != firstMin:
                secondMin = min(secondMin, node.val)

            if node.left:
                deque.append(node.left)
                deque.append(node.right)

        return secondMin if secondMin != float('inf') else -1
