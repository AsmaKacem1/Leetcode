class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        my_set=set()
        for i in range(len(sentence)):
            my_set.add(sentence[i])
        return len(my_set)==26
            
        