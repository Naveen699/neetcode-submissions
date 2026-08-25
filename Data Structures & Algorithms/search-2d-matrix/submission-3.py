class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:

        for i in range(len(nums)): 
            if target >= nums[i][0] and target <= nums[i][-1]:
                
                left, right = 0, len(nums[i]) - 1

                while left <= right: 
                    middle = left + (right - left) // 2
                    
                    if target == nums[i][middle]: 
                        return True 
                    
                    if target > nums[i][middle]:
                        left = middle + 1

                    if target < nums[i][middle]:
                        right = middle - 1
                
        
        return False
        