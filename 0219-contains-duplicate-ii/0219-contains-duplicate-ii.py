class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for i,j in enumerate(nums):
            if (j in dic) and (i-dic[j]<=k):
                return True
            dic[j]=i
        return False