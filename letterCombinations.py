https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comnbinations = []
        phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        def helper(digits, string):
            if not digits:
                comnbinations.append(string)
                return

            for char in phone.get(digits[0]):
                helper(digits[1:], string + char)

        if digits:
            helper(digits, '')
        return comnbinations
