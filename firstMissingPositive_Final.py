class Solution:
       #https://leetcode.com/problems/first-missing-positive/submissions/
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        
        
        for i in range(len(nums)): 
            index = nums[i]%n 
            nums[index] += n
        
        for i in range(1,len(nums)):
            if nums[i]//n == 0:
                return i
        return n
