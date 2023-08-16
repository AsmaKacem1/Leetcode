class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        dic1 = Counter(s1)
        window = Counter(s2[:len_s1])
        
        for end in range(len_s1, len_s2):
            if window == dic1:
                return True
            
            window[s2[end]] += 1
            window[s2[end - len_s1]] -= 1
            
            if window[s2[end - len_s1]] == 0:
                del window[s2[end - len_s1]]
        
        return window == dic1


