https://leetcode.com/problems/min-stack/description
Design a stack that supports getMin() in O(1) time and O(1) extra space

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        min_item = x
        if self.stack:
            min_item = min(min_item, self.getMin())
        self.stack.append(x)
        self.minstack.append(min_item)     

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
