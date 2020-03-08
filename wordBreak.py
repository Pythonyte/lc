https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Amazing Solution
        wordlen = len(s)+1
        dic = set(wordDict)
        dp = [False] * wordlen
        dp[0] = True
        for i in range(wordlen):
            for j in range(i+1,wordlen):
                if s[i:j] in dic and dp[i]:
                    dp[j] = True
        return dp[-1]
                
                    
        
        
        
