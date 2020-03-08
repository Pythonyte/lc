https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            count = [0]*26
            for char in word:
                char = char.lower()
                count[ord(char) - ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = [word]
            else:
                ans[tuple(count)].append(word)
        return ans.values()
        
