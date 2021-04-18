# https://leetcode.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
        # To change the chars in place, we have to maintain write index
        anchor = write = 0
        
        
        for read, c in enumerate(chars):
            
            # If reached to last char OR
            # If next char is different char
            if read + 1 == len(chars) or chars[read + 1] != c:
                # Update chars 
                chars[write] =  chars[anchor]
                write += 1
                
                # if char occurred more than 1
                if read > anchor:
                    freq = read - anchor + 1
                    for digit in str(freq):
                        # Update chars 
                        chars[write] = digit
                        write += 1
                
                # Change anchor only when new diff char comes
                anchor = read + 1
        return write
            
