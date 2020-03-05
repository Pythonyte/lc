https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1: return n
        lis = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j]+1:
                    lis[i] = lis[j] + 1
        
        max_lis = 0
        for item in lis:
            max_lis = max(max_lis, item)
        return max_lis
