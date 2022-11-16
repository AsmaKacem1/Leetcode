# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        height=n
        while low<=height:
            res=(height+low)//2
            if guess(res)==0:
                return res
            elif guess(res)==-1:
                height=res-1
            else:
                low=res+1

            
        