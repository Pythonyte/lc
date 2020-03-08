https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0:1}
        curr_sum = 0
        total_arrays = 0
        # Traverse through the given array
        for item in nums:
            curr_sum += item

            if curr_sum - k in hash_map:
                print(curr_sum - k, curr_sum, hash_map[curr_sum - k], total_arrays)
                total_arrays += hash_map[curr_sum - k]
            
            if curr_sum in hash_map:
                    hash_map[curr_sum] += 1
            else:
                hash_map[curr_sum] = 1
            
        return total_arrays
