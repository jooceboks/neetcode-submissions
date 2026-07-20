class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) # number, freq
        
        for num in nums:
            freq[num] += 1
        
        topfreq = sorted(freq, key = lambda number:freq[number], reverse = True)
        return topfreq[:k]