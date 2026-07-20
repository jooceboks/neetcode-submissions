class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s.strip()
        seen = defaultdict(int) #char, index

        l = 0
        r = 0
        maxlen = 0

        while r < len(s):
            char = s[r] 
            if char in seen:
                l = max(l, seen[char] + 1)
            seen[char] = r
            maxlen = max(maxlen, r - l + 1)
            r +=1
        return maxlen