class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for j in range(len(nums)-1,1,-1):
            if (nums[j]<(nums[j-1]+nums[j-2])) :
                return nums[j]+nums[j-1]+nums[j-2]
        
        return 0
        