class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        result=0
        for i in nums:
            dic[i]+=1
        for num in dic:
            result+=(dic[num]*(dic[num]-1))//2
        return result
        