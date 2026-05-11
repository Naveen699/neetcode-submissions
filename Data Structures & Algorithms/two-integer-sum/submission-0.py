class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in freq:
                return [freq[difference], i]
            freq[n] = i
        return None