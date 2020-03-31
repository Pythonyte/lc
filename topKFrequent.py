class Solution:
    # Non Pythonic Solution
    def topKFrequentOLD(self, nums: List[int], k: int) -> List[int]:
        def get_val_freq_map(nums):
            val_freq_map = {}
            for num in nums:
                if num not in val_freq_map:
                    val_freq_map[num] = 0
                val_freq_map[num] += 1
            return val_freq_map
        
        def get_freq_vals_map(val_freq_map):
            freq_vals_map = {}
            for item, freq in val_freq_map.items():
                if freq not in freq_vals_map:
                    freq_vals_map[freq] = []
                freq_vals_map[freq].append(item)
            return freq_vals_map
        
        def get_itmes_based_on_frequency(freq_vals_map, nums, k):
            output = []
            for freq in range(len(nums), 0, -1):
                if freq in freq_vals_map:
                    for item in freq_vals_map[freq]:
                        if len(output) == k:
                            break
                        output.append(item)
            return output
        
        val_freq_map =  get_val_freq_map(nums)
        freq_vals_map = get_freq_vals_map(val_freq_map)
        output = get_itmes_based_on_frequency(freq_vals_map, nums, k)
        print(val_freq_map,freq_vals_map,output)
        return output
    
    
    # Pythonic Solution 1
    def topKFrequentP1(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        val_freq_map = defaultdict(int)
        for num in nums:val_freq_map[num] += 1
        return sorted(val_freq_map, key=val_freq_map.get, reverse=True)[:k]
    
    # Pythonic Solution 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 
