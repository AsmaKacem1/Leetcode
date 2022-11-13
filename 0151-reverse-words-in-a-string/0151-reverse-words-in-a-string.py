class Solution:
    def reverseWords(self, s: str) -> str:
        List=list(s.split(' '))
        List.reverse()
        while '' in List:
            List.remove('')
        return " ".join(List)
        