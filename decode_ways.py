https://leetcode.com/problems/decode-ways/description/
class Solution:
#     def create_mapping(self):
#         mapping = {}
#         for num in range(ord('A'), ord('Z')+1):
#             mapping[chr(num)] = num - ord('A') + 1
#         return mapping
    
#     def create_reverse_mapping(self):
#         mapping = {}
#         for num in range(1, 27):
#             mapping[num] = chr(num + ord('A') - 1)
#         return mapping
    
#     def numDecodings(self, s: str) -> int:
#         mapping = self.create_reverse_mapping()
#         combinations = []
        
#         def helper(s, combs):
            
#             if not s:
#                 combinations.append(combs)
#                 return 
#             if s[0] == '0': return
#             if len(s) >= 1 and int(s[:1]) > 0:
#                 helper(s[1:], combs + [s[:1]])
#             if len(s) >= 2 and 0 < int(s[:2]) <= 26:
#                 helper(s[2:], combs + [s[:2]])
            

#         helper(s, [])
#         print(combinations)
#         return len(combinations)
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]
