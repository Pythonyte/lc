https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for char in s:
            if char in mapping:
                stack.append(mapping[char])
            else:
                if not stack: return False
                sign = stack.pop()
                if char != sign: return False
        if stack: return False
        return True
            
