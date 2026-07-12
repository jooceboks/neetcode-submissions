class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens = defaultdict(int)
        seent = defaultdict(int)
        for char in s:
            seens[char] +=  1

        for char in t:
            seent[char] +=  1    

        if seens == seent:
            return True
        return False   