class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=max(nums)
        res=0
        for i in range(len(nums)):
            if nums[i]>=0:
                res+=nums[i]
                if res>maxi:
                    maxi=res
            if nums[i]<0:           
                res+=nums[i]
                if res>maxi:
                    maxi=res
                if res<0:
                    res=0
        return maxi