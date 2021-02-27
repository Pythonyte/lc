https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)
        
        left = [0]*n
        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(left[i-1], height[i])
        
        right = [0]*n
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        water = 0
        for i in range(n):
            water = water + min(left[i], right[i]) - height[i]
        
        return water
        

        
###Optimized Approach 

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -=1
        return areas
