class Solution:
    def maximum69Number (self, num: int) -> int:
        str1=str(num)
        str1=str1.replace('6','9',1)
        return int(str1)
        