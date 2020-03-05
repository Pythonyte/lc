https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        allowed_range = list(range(ord('A'),ord('Z')+1)) + list(range(ord('a'),ord('z')+1)) + list(range(ord('0'),ord('9')+1))
        while start < end:
            if ord(s[start]) not in allowed_range:
                start += 1
                continue
            if ord(s[end]) not in allowed_range:
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
            
            
