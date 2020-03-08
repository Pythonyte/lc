https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     length = len(s)
    #     lps = ''
    #     for i in range(length):
    #         for j in range(i+1, length+1):
    #             if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(lps):
    #                 lps = s[i:j]          
    #     return lps
    
    def longestPalindrome(self, s: str) -> str: 
        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)]  

        maxLength = 1
        i = 0
        while (i < n) : 
            table[i][i] = True
            i = i + 1

        start = 0
        i = 0
        while i < n - 1 : 
            if (s[i] == s[i + 1]) : 
                table[i][i + 1] = True
                start = i 
                maxLength = 2
            i = i + 1

        k = 3
        while k <= n : 
            i = 0
            while i < (n - k + 1) : 
                j = i + k - 1
                if (table[i + 1][j - 1] and s[i] == s[j]) : 
                    table[i][j] = True

                    if (k > maxLength) : 
                        start = i 
                        maxLength = k 
                i = i + 1
            k = k + 1
        return s[start:start+maxLength]
