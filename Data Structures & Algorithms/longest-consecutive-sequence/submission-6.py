class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        numbers = list(numbers)
        numbers.sort()
        print(numbers)


        maxseq = 1 
        curr = 1

        if len(numbers) == 0:
            return 0 
        for i in range(len(numbers) - 1):
            if numbers[i+1] - numbers[i] == 1:
                curr += 1
                maxseq = max(maxseq, curr)
            else:
                curr = 1
        return maxseq        

