class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sequence = set(nums)
        longest = 0


        for i in sequence: 
            if i - 1 not in sequence: 
                length = 1

                while i + length in sequence: 
                    length += 1

                longest = max(longest, length)


        return longest

            





