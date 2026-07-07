class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for string in strs:
            key = tuple(sorted(string))
            result[key].append(string)
        return list(result.values())
