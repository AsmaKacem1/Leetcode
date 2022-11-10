class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
        while a<=b:
            x=a+(b-a)//2
            if (nums[x]==target):
                return x
            elif nums[x]<target:
                res=x+1
                a=x+1
            else:
                res=x
                b=x-1
              
        return res
        