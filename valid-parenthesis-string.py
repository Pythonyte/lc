# https://leetcode.com/problems/valid-parenthesis-string/submissions/

class Solution:
    # def checkValidString(self, s: str) -> bool:
    #     stack, strc_count = [], 0
    #     for c in s:
    #         if c == '(':
    #             stack.append(')')
    #         elif c == '*':
    #             strc_count += 1
    #         elif c == ')':
    #             if stack:
    #                 stack.pop()
    #             elif strc_count:
    #                 strc_count -= 1
    #             else:
    #                 return False
    #     if stack and len(stack) != strc_count:
    #         return False
    #     return True
    def checkValidString(self, s):
        stack = []
        for c in s:
            if c in '(*':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        
        print(stack)
        stars = []
        parens = []

        for i, c in enumerate(stack):
            if c == '*':
                stars.append((i, c))
            elif c == '(':
                parens.append((i, c))
            else:  # c == ')'
                if parens:
                    parens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        print(stars, parens)
        while parens:
            i, c = parens.pop()
            if not stars:
                return False
            if stars[-1][0] < i:
                return False
            stars.pop()        

        return True
