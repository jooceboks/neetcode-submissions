class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) # num, freq

        for num in nums:
            freq[num] += 1
        
        results = []
        output = []
        for item in freq.items():
            results.append([item[1], item[0]])
            results.sort(reverse = True) # sort by count greatest - least
        for i in results:
            output.append(i[1])
        return output[:k]
