class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for index, element in enumerate(nums):
            
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            l, r = index + 1, len(nums) - 1

            while l < r: 
                threeSum = element + nums[l] + nums[r]
                if threeSum > 0: 
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else: 
                    result.append([element, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return result