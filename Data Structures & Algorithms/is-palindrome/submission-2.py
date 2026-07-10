class Solution:
    def isPalindrome(self, s: str) -> bool:
        ignore = ["!", "?", "/", " ", ",", "'", ".", "%", ":"]
        s = s.lower()
        left = 0
        right = len(s) - 1 
        i= 0
        while i < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            elif s[left] in ignore:
                left += 1
            elif s[right] in ignore:
                right -= 1
            else:
                return False
        return True        
