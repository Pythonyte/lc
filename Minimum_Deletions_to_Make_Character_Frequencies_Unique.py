# Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        used_freqs = set()
        res = 0
        
        for char, freq in freq_map.items():
            while freq and freq in used_freqs:
                freq -= 1
                res += 1
            used_freqs.add(freq)
        return res
