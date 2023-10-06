class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3: return n-1
        k,r=divmod(n,3)
        if r==1:
            r=4
            k-=1
        ans=3**k
        if r>0: ans*=r
        return ans
        