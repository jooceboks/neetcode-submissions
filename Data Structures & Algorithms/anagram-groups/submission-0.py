class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        j = defaultdict(list) # [][]
        for string in strs: # loop words
            counts = [0]*26
            for char in string: 
                counts[ord(char) - ord('a')] +=1      
            j[tuple(counts)].append(string)
        result = j.values()
        return list(result)