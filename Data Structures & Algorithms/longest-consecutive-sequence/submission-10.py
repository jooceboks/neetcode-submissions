class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxlen = 0

        for num in numbers:
            if (num - 1) not in numbers:
                length = 1
                while (num + length) in numbers:
                    length +=1 
                maxlen = max(length, maxlen)
        return maxlen        



