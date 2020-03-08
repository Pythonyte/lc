# https://leetcode.com/problems/design-compressed-string-iterator/description/
# Design String Decompress iterator class with next() and hasnext() methods
# tes4t =>
# Each next should print following seq.
# t, e, s, s, s, s, t

class StringIterator:

    def __init__(self, compressedString: str):
        import re
        self.tokens = []
        # This will store each letter and its count in array
        
        # L1E22C3 will be [(L, 1), (E, 22), (C, 3)]
        for token in re.findall('\D\d+', compressedString):
            self.tokens.append((token[0], int(token[1:])))
        
        # Reversing the array so that popping and appending to array will be O(1) time and easier
        self.tokens = self.tokens[::-1]


    def next(self) -> str:
        if not self.tokens: return ' '
        
        char, counter = self.tokens.pop()
        counter -= 1
        
        # Add into tokens if counter > 0, means still have that char
        if counter:
            self.tokens.append((char, counter))
        return char

    def hasNext(self) -> bool:
        return bool(self.tokens)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
