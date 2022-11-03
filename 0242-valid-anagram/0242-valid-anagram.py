class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        if len(s)!=len(t):
            return False
        for i in range (len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        for i in range (len(t)):
            if  t[i] not in dic:
                return False
            if dic[t[i]] and dic[t[i]]>0:
                dic[t[i]]-=1
            else:
                return False
        return True
        