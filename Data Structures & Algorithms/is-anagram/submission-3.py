class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        S = [0]*26
        T = [0]*26

        for char in s:
            S[ord(char) - ord('a')] += 1
        for char in t:
            T[ord(char) - ord('a')] += 1    

        if S == T:
            return True
        return False        