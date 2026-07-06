class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indice = {}

        for index, number in enumerate(nums):
            indice[number] = index

        for index, number in enumerate(nums):
            difference = target - number
            if difference in indice and index != indice[difference]:
                return [index, indice[difference]]
            
        return []
