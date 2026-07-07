class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for i in strs:
            frequency = [0] * 26
            for c in i:
                frequency[ord(c) - ord('a')] += 1
            results[tuple(frequency)].append(i)
        return list(results.values())