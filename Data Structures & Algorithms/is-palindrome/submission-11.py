class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s[l].isalnum() == False:
                l+=1
            while l < r and s[r].isalnum() == False:
                r-=1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
  


