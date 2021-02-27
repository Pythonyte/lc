https://leetcode.com/problems/product-of-array-except-self/description/
#  Please solve it without division and in O(n).
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [0]*length
        
        output[0] = 1
        for i in range(1, length):
            output[i] = nums[i-1] * output[i-1]
        
        rightmost = 1
        for i in range(length-1, -1, -1):
            output[i] *= rightmost
            rightmost *= nums[i]
        
        return output
