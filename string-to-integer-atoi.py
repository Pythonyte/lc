https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        
        Neg = False

        try:         
            while str[0] == " ":
                str = str[1:]
        except:
            return 0

        try:      
            if (str[0] in "+-"):
                if str[0] =="-":
                    Neg = True
                str = str[1:]

        except:
            return 0        

        for i in range(0,len(str)):
            if str[i].isnumeric():
                continue           
            else:
                i+=-1
                break

        try:
            str = int(str[:i+1])       
        except:
            return 0 

        if Neg:
            return max((-2**31),-str)

        else:
            return min((2**31)-1,str)
