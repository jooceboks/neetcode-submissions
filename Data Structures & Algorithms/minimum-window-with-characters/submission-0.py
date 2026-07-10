class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t not in s return ""

        td = defaultdict(int) #char, count
        for char in t:
            td[char] += 1

        window = defaultdict(int) # char, count
        have = 0
        need = len(td)
        left = 0
        minlen = float("inf")
        result = [-1, -1]
        
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in td and window[char] == td[char]:
                have += 1
            while have == need:
                if right - left + 1 < minlen:
                    result = [left,right]
                    minlen = right - left + 1    
                window[s[left]] -= 1
                if s[left] in td and window[s[left]] < td[s[left]]:
                    have -= 1
                left+=1
        left = result[0]
        right = result[1]
        return s[left:right + 1] if minlen != float("inf") else ""



