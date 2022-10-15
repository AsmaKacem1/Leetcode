class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        res=-1
        for i in range (len(s)):
            if (s[i] in dic):
                dic[s[i]]=-1
            else:
                dic[s[i]]=i
        for i in dic:
            if dic[i]!=-1 :
                return dic[i]
        
        return res
        