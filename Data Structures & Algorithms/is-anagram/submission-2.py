class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        S = defaultdict(int) 
        T = defaultdict(int)
        
        for char in s:
            S[char] += 1

        for char in t:
            T[char] += 1

        if S == T:
            return True
        else:
            return False
