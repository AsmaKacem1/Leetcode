class Solution:
    def reverseVowels(self, s: str) -> str:
        L={'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        i=0
        j=len(s)-1
        while i<j:
            if (s[i] in L) and (s[j] in L):
                
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif  (s[i] in L):
                j-=1
            else:
                i+=1
        return "".join(s)
        