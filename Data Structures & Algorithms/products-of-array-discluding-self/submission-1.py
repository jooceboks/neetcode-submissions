class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # total product / nums[i]
        # division by 0 return 0
        # if 2 zeros in list product = 0
        # if only one then product 1 = 0 product 2 everything buy zero 

        total = 1
        result = []
        countzero = 0

        for num in nums:
            if num == 0:
                countzero += 1
            else:
                total *= num

        for num in nums:
            if countzero > 1:
                result.append(0)   
            elif countzero == 1 and num !=0:
                result.append(0) 
            elif countzero == 1 and num == 0:
                result.append(total)
            else:
                result.append(total//num) 

        return result              


