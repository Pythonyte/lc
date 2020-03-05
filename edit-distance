https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        cost_add = cost_remove = cost_replace = 1
        for r in range(rows):
            for c in range(cols):
                if r == 0: 
                    dp[r][c] = c
                elif c == 0: 
                    dp[r][c] = r
                elif word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(
                        dp[r-1][c-1] + cost_replace,
                        dp[r][c-1] + cost_add,
                        dp[r-1][c] + cost_remove
                    )
        return dp[rows-1][cols-1]
        
