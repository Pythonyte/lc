"""
https://leetcode.com/problems/3sum/
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        target = 0
        nums.sort()
        for i in range(len(nums)-2):
            # index of the first element in the remaining elements 
            l = i + 1 

            # index of the last element 
            r = len(nums)-1 
            
            # Below condition is only for target = 0, if i is positive no, all possible numbers for l and r will be positive only
            #which will naver make triplet 0, so break from here
            if nums[i]>0: 
                break 
            if i>0 and nums[i]==nums[i-1]: 
                continue
            while l < r:
                triplet_sum = nums[i] + nums[l] + nums[r]
                if triplet_sum == target:
                    output.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l += 1
                    r -= 1
                elif triplet_sum < target:
                    l += 1
                elif triplet_sum > target:
                    r -= 1
                    
        return output
