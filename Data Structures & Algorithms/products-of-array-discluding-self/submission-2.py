class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []
        zerocount = 0
    
        for num in nums:
            if num == 0:
                zerocount += 1
            else:
                product *= num

        for num in nums:
            if zerocount > 1:
                result.append(0)

            elif zerocount == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product//num)
        return result
