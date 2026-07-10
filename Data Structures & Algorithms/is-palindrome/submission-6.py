class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for c in s:
            if ord("a") <= ord(c.lower()) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
                cleaned.append(c.lower())
        return cleaned == cleaned[::-1]
