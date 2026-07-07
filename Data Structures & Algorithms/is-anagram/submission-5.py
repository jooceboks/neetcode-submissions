class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        S = [0]*36 
        T = [0]*36 

        for char in s:
            S[ord(char) - ord('a')] += 1  

        for char in t:
            T[ord(char) - ord('a')] += 1  
        
        if S == T:
            return True
        return False