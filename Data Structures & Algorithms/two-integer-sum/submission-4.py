class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort() 

        left = 0
        right = len(A) - 1
        while left < right:
            if A[left][0] + A[right][0] < target:
                left +=  1
            elif A[left][0] + A[right][0] > target:       
                right -=  1
            else:    
                if A[left][1] > A[right][1]:
                    return [A[right][1], A[left][1]]
                else: 
                    return [A[left][1], A[right][1]]
