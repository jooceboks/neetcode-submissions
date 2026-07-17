class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sublist = defaultdict(list) #list, words

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1 
            sublist[tuple(count)].append(word)
        return list(sublist.values())    