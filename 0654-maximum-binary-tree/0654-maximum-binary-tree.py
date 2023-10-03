# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maxi(nums):
            maxi=0
            result=0
            for i in range(len(nums)):
                if nums[i]>maxi:
                    result=i
                    maxi=nums[i]
            return result
        def constructTree(nums):
            if not nums:
                return None
            index=maxi(nums)
            root=TreeNode(nums[index])
            root.left=constructTree(nums[:index])
            root.right=constructTree(nums[index+1:])
            return root
        return constructTree(nums)

        