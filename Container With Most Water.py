class Solution:
    # @return an integer
    def maxArea(self, height):
        maxVal=min(height[0], height[-1])*(len(height)-1)
        left=-1
        i=0
        while i<len(height)-1:
            if height[i]>height[left]:
                j=len(height)-1
                right=len(height)-1
                while j>i:
                    if height[j]>=height[right]:
                        maxVal=max(maxVal, min(height[j], height[i])*(j-i))
                        right=j
                    j-=1
                left=i
                right=len(height)-1
            i+=1
            maxVal=max(maxVal, min(height[i], height[-1])*(len(height)-1-i))
        return maxVal
