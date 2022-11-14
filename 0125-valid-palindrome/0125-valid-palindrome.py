class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1=""
        for i in s:
            if i.isalpha():
                res1+=i.lower()
            if i.isnumeric():
                res1+=i
        
        res2=res1 [::-1]
        print (res1)
        return res2==res1