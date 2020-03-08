https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
