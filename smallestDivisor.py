# Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def helper(left, right):
            m = (left + right) // 2
            
            if left >= right:
                nonlocal ans
                ans = left
                return 
        
            total = sum(math.ceil(num/m) for num in nums)
                
            # Try dividing by bigger numbers if total is bigger
            if total > threshold:
                helper(m+1,right)
            # If total is lesser than thrashold then check for more smaller divisor
            else:
                helper(left, m)
            
        ans = None
        helper(1, max(nums))
        return ans
