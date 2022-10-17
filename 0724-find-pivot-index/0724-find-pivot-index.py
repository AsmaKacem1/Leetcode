class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            nums1=nums[:i]
            nums2=nums[i+1:]
            leftsum=sum(nums1)
            if (leftsum==sum(nums2)):
                return i
        return -1
        