https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]: return False
                start += 1
                end -= 1
            return True
        
        start, end = 0, len(s)-1
        while start < end and s[start] == s[end]:
            start += 1
            end -= 1
        
        if ispalindrome(s, start+1, end):
            print(start, s[start])
            return True
        
        if ispalindrome(s, start, end-1):
            print(end, s[end])
            return True
        
        return False
