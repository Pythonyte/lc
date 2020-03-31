https://www.youtube.com/watch?v=P63aaiRFECU
https://leetcode.com/problems/find-median-from-data-stream/description/

# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.nums = []
#         self.count = 0
#         self.median = []
        
#     def addNum(self, num: int) -> None:
#         self.nums.append(num)
#         self.count += 1
#         self.nums.sort()
    
#     def findMedian(self) -> float:
#         index = self.count//2
#         if self.count % 2 == 0:
#             self.median = (self.nums[index-1] + self.nums[index])/2
#         else:
#             self.median = self.nums[index]
#         return self.median


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        first_half_max_heap  = max_heap
        scnd_half_min_heap = min_heap
        """
        self.max_heap = []
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        
        if self.max_heap and num < self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        elif self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            # for first and second element (6, 10) or (6, 5)
            heapq.heappush(self.max_heap, -num)
        
        if len(self.max_heap) - len(self.min_heap) == 2:
            num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, num)
        elif len(self.min_heap) - len(self.max_heap) == 2:
            num = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, num)
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2 
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
            
    
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
