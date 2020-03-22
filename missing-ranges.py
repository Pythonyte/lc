https://leetcode.com/problems/missing-ranges/description/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing_ranges = []
        num = lower - 1
        prev = None
        
        def get_val(v1, v2):
            if v1 == v2:
                return str(v1)
            return "{}->{}".format(v1, v2)
        
        for num in nums:
            # Check for duplicate numbers
            if prev and prev == num:
                continue
            
            if num == lower:
                lower += 1
            else:
                missing_ranges.append(get_val(lower, num-1))
                lower = num + 1
            prev = num
        else:
            # check if list ends but max range is not yet reached
            # last num should not be max range
            # last num should be less than max range
            if num != upper and num < upper: 
                val = "{}->{}".format(num+1, upper)
                missing_ranges.append(get_val(num+1, upper))
        return missing_ranges
