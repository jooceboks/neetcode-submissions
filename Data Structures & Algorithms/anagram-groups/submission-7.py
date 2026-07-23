class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #count, list of words

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())