class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set=set()
        l,result=0,0
        for r in range(len(s)):
            while(s[r] in new_set):
                new_set.remove(s[l])
                l+=1
            new_set.add(s[r])
            result=max(result,r-l+1)
        return result
            
        