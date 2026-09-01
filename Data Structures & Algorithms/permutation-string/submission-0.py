class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1freq = {}

        for i in s1: 
            s1freq[i] = s1freq.get(i, 0) + 1

        
        seen = len(s1freq)
        for i in range (len(s2)):
            s2freq, cur = {}, 0
            for j in range(i, len(s2)):
                s2freq[s2[j]] = s2freq.get(s2[j], 0) + 1
                if s1freq.get(s2[j], 0) < s2freq[s2[j]]:
                    break
                if s1freq.get(s2[j], 0) == s2freq[s2[j]]:
                    cur += 1
                if cur == seen: 
                    return True
        
        return False
                