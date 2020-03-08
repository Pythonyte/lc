https://leetcode.com/problems/maximum-subarray/description/
https://www.geeksforgeeks.org/size-subarray-maximum-sum/

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     import sys
    #     max_sum = -sys.maxsize 
    #     max_ending_here = 0
    #     for i, item in enumerate(nums):
    #         max_ending_here += item
    #         max_sum = max(max_sum, max_ending_here)
    #         end_index = i
    #         if max_ending_here < 0:
    #             max_ending_here = 0
    #     return max_sum
    
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_sum = -sys.maxsize 
        max_ending_here = 0
        start_index, end_index, s = 0, 0, 0
        
        for i, item in enumerate(nums):
            max_ending_here += item
            
            if max_ending_here > max_sum:
                max_sum = max_ending_here
                start_index = s
                end_index = i
                
            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1
        
        print(start_index, end_index, max_sum)
        return max_sum
