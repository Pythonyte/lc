class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k > len(nums): return -1
        heap = []
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        return heap and heap[0]
