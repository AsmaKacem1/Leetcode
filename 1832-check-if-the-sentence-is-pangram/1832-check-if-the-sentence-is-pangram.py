class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ch=''
        for i in range(len(sentence)):
            if not (sentence[i] in ch):
                ch+=sentence[i]
        return len(ch)==26
            
        