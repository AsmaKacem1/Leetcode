class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            r=sum(nums[i+1:len(nums)])
            l=sum(nums[0:i])
            print(l)
            print(r)
            if(r==l):
                return i
        return -1