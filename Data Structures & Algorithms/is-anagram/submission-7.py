class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = [0]*36
        tt = [0]*36

        for char in s:
            ss[ord(char) - ord("a")]+= 1
        
        for char in t:
            tt[ord(char) - ord("a")]+= 1

        if ss == tt:
            return True
        return False    

