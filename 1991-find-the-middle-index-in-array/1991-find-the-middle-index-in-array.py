class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        r=sum(nums)
        l=0
        for i in range(len(nums)):
            if l==r-nums[i]:
                return i
            l+=nums[i]
            r-=nums[i]
        return -1