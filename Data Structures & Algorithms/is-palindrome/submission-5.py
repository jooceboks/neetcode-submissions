class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ignore = ["!", "?", "/", " ", ",", "'", ".", "%", ":"]
        s = s.lower()
        left = 0
        right = len(s) - 1 
        i= 0
        while i < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            elif not (ord("a") <= ord(s[left]) <= ord("z")) and not (ord("0") <= ord(s[left]) <= ord("9")):
                left += 1
            elif not (ord("a") <= ord(s[right]) <= ord("z")) and not (ord("0") <= ord(s[right]) <= ord("9")):
                right -= 1
            else:
                return False
        return True        
