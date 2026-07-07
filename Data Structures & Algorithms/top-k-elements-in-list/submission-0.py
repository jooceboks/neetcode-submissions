class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        t = defaultdict(int) 

        for num in nums:
            t[num] += 1

        items = list(t.items()) # (key, val)
        print(str(items))
        j = []
        for item in items:
            j.append([item[1], item[0]])
        print(j)
        j.sort(reverse = True)    
        print(j)
        m = []
        for i in range(k):
            m.append(j[i][1]) 
        return m
            