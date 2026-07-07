class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zcount = 0 
        for i in nums:    
            if i == 0:
                zcount +=1
                if zcount > 1:
                    product = 0
                    break
                else:
                    continue                
            product *= i

        results = []
        for j in range(len(nums)):
            if zcount > 1:
                results.append(0)
            elif zcount == 1:
                if nums[j] == 0:
                    results.append(product)
                else:
                    results.append(0)
            else:
                results.append(product // nums[j])      
        return results