class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        #get frequency map 
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        
        for n in nums: 
            freq[n] = 1 + freq.get(n, 0)

        



        #append freq map to array of arrays
        for number, c in freq.items(): 
            count[c].append(number)
        


        #get top k elements from array and append to res
        res = []

        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                res.append(j)
            
            if len(res) == k:
                return res
        
        return res

        
