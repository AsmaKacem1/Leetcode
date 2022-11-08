class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)==1:
            return s
        i=0
        n=len(s)
        while i<(n-1):
            if (s[i].lower()==s[i+1].lower()) and (s[i]!=s[i+1]):
                s=s.replace(s[i]+s[i+1], '')
                i=0
                n=len(s)
            else:
                i+=1

        return s
            