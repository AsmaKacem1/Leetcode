class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        total=0
        for i,num in enumerate(nums):
            total+=num
            r=total%k
            if not r in dic:
                dic[r]=i
            elif i-dic[r]>1:
                return True
        return False
            
            