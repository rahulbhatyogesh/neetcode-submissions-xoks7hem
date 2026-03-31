class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        volume = 0
        while (i<j):
            if ((min(heights[i], heights[j]))*(j-i)) > volume:
                volume = (min(heights[i], heights[j]))*(j-i)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return volume