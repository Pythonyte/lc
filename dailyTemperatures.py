# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, result = [], [0]*len(T)
        
        # start loop from end
        for i in range(len(T)-1, -1, -1):
            # Remove elements untill these are smaller than current element, for upcoming elements, those smaller elements of no use
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((T[i], i))
        return result



