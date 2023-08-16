class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1=Counter(s1)
        window=Counter(s2[:len(s1)])
        for start in range(len(s1),len(s2)):
            if dic1==window:
                return True
            window[s2[start]]+=1
            window[s2[start-len(s1)]]-=1
            if window[s2[start-len(s1)]]==0:
                del window[s2[start-len(s1)]]
            
        return dic1==window

        
      