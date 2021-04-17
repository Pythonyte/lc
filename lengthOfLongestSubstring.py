class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Longest Substring Without Repeating Characters
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/
        :param s:
        :return:
        """
        ans = 0
        mp = {}
        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j-i+1)
            mp[s[j]] = j + 1
        return  ans