class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Make k size heap, where k largest elements are present from nums array, 
        # where root is minimum element means kth largest as heap size is k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def add(self, val: int) -> int:
        # Push item in heap 
        # 1. if heap size if less than k (we can still fill heap)
        # 2. if val is greater than minimum element of heap, so root of heap is no more kth largest
        if len(self.heap) < self.k or val > self.heap[0]:
            heapq.heappush(self.heap, val)
        
        # in case we pushed element in heap and heapsize gets bigger than k, remove one element from heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
