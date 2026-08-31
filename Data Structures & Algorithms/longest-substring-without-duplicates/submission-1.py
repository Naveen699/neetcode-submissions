class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        left = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen: 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[r])
            longest = max(longest, r - left + 1)
        
        return longest
            
