class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return ""

        store = defaultdict(list) # count, word
        for word in strs:
            count = [0]*36
            for char in word:
                count[ord(char) - ord("a")] += 1
            store[tuple(count)].append(word)

        return list(store.values())     
                
