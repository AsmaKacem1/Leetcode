class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(ransomNote)==len(magazine)==1):
            return ransomNote==magazine
        elif (len(ransomNote)>len(magazine)):
                return False
        else:
            for i in ransomNote:
                if i in magazine:
                    magazine=magazine.replace(i,'',1)
                else:
                    return False
            return True