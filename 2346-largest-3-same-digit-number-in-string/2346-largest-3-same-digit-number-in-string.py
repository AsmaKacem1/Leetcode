class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxi=-1
        for i in range(len(num)-2):
            if (num[i]==num[i+1] and num[i+2]==num[i+1]):
                maxi=max(maxi,int(num[i]))
                i+=2
        if maxi==-1:
            return ""
        else:
            x=3*str(maxi)
            return x
            
        