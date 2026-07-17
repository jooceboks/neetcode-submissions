class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #area = distance * lowerheight

        i = 0
        j = len(heights) - 1
        maxarea = 0
        while i < j:
            distance = j - i
            
            lowerheight = min(heights[i], heights[j])
            currarea = distance * lowerheight

            if currarea > maxarea:
                maxarea = currarea

            if heights[i] < heights[j]:
                i += 1
            else: 
                j-=1
        return maxarea

