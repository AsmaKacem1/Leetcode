class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        som,l,res=0,0,float("inf")
        for r in range(len(nums)):
            som+=nums[r]
            while som>=target:
                res=min(res,r-l+1)
                som-=nums[l]
                l+=1
        return 0 if res==float("inf") else res
                
                
                
        