https://leetcode.com/problems/sliding-window-maximum/description/

class Solution:
    # Time O(nk)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        def get_max(i):
            import sys
            val = -sys.maxsize
            for num in nums[i:i+k]:
                val = max(val, num)
            return val
        
        return [get_max(i) for i in range(0, len(nums)-k+1)]
    
    # Time O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0: return []
        if k == 1: return nums
        
        dq = deque([])
        output = []
          
        # Use deque here (STORING INDEX ON DEQUE NOT VALUE... REMEMBER IT!!!)
        # Idea is to maintain deque in such a way that
        # 1. always max element is in top (deque[0])
        # 2. if top element is out of window, remove from front of deque (popleft)
        # 3. when a new value comes, remove all elements from deque from last (pop) till elements are smaller than value
        #    so no smaller values which will never be the ans are not in deque
        def clean_deque(i):
            # Case2 if top element is out of window, remove from front of deque (popleft)
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # 3. when a new value comes, remove all elements from deque from last (pop) till elements are smaller than value
            #    so no smaller values which will never be the ans are not in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
        
        # for first k elements
        for i in range(k):
            clean_deque(i)
            dq.append(i)
        
        output.append(nums[dq[0]])
        for i in range(k,len(nums)):
            clean_deque(i)
            dq.append(i)
            output.append(nums[dq[0]])
        
        return output
    
    """
    Example:
        6,5,7,10,6,5,3,20
        k = 3
        Queue:  
            => 6 <=
            => 6 5 <=
            => 7 <=
            => 10 <=
            => 10, 6 <=
            => 10, 6, 5 <=
            => 6, 5, 3 <=
            => 20 <=
    """
