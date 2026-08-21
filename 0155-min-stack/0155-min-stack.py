class MinStack:

    def __init__(self):
        self.stack = [] # stores (element, min_ele) 
        
    def push(self, value: int) -> None:
        min_ele = value if not self.stack else min(self.stack[-1][1], value)
        self.stack.append((value, min_ele))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()