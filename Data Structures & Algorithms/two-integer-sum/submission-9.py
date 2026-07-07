class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:    
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])