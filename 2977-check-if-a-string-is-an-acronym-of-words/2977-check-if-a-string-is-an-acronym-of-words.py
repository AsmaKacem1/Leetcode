class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        result=""
        for i in range(len(words)):
            result+=words[i][0]
            if result!=s[:i+1]:
                return False
          
        return result==s