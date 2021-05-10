# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        intervals = sorted(intervals, key=lambda x:x[0])
        output = []
        start, end = intervals[0][0], intervals[0][1]
        
        for s,e in intervals[1:]:
            if s <= end:
                end = max(e,end)
            else:
                output.append([start, end])
                start, end = s, e
        output.append([start,end])
        return output
                
