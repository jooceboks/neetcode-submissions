class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]
        post = [1]
        results  = []
        for i in range(len(nums) - 1):
            pre.append(pre[-1] * nums[i])
            
        for i in range(len(nums)-1, 0, -1):
            post.append(post[-1]*nums[i])
        
        post.reverse()
        
        for i in range(len(nums)):
            results.append(pre[i]*post[i])

        return results
