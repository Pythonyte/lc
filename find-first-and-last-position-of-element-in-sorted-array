https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftsearch(nums, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if target < nums[mid]:
                return leftsearch(nums, start, mid-1, target)
            elif target > nums[mid]:
                return leftsearch(nums, mid+1, end, target)
            else:
                if mid and nums[mid] == nums[mid-1]:
                    return leftsearch(nums, start, mid-1, target)
                return mid
        
        def rightsearch(nums, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if target < nums[mid]:
                return rightsearch(nums, start, mid-1, target)
            elif target > nums[mid]:
                return rightsearch(nums, mid+1, end, target)
            else:
                if mid < end and nums[mid] == nums[mid+1]:
                    return rightsearch(nums, mid+1, end, target)
                return mid
        
        left_index = leftsearch(nums, 0, len(nums)-1, target)
        right_index = rightsearch(nums, 0, len(nums)-1, target)
        print(left_index, right_index)
        return [left_index, right_index]
                    
                
            
