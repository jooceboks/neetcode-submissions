class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        t = defaultdict(int) # number , count

        
        for num in nums:
            t[num] += 1

        t = sorted(t, key = lambda x: t[x], reverse=True)
        return t[:k]
        
        

        