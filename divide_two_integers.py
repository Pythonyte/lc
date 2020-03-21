#https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

        min_size, max_size = -2**31, 2**31-1
        dividend_sign = -1 if dividend < 0 else 1
        divisor_sign = -1 if divisor < 0 else 1
        divisor, dividend= abs(divisor), abs(dividend)
        quotient = 0
        
        while dividend >= divisor:
            val, power = divisor, 1
            while val+val < dividend:
                val += val
                power += power
            
            quotient += power
            dividend -= val
        
        quotient = quotient * dividend_sign * divisor_sign
        quotient = min(quotient, max_size)
        quotient = max(quotient, min_size)
        
        return quotient
