# Last updated: 8/18/2025, 6:40:32 PM
import heapq
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minVal = None

        

    def push(self, val: int) -> None:
        if self.minVal is None or self.minVal > val:
            self.minVal = val
        
        self.stack.append([val, self.minVal])



    def pop(self) -> None:
        tmp = self.stack[-1]
        self.stack = self.stack[:-1]
        if len(self.stack)==0:
            self.minVal = None
            return
        if self.stack[-1][1]!=self.minVal:
            self.minVal = self.stack[-1][1]


    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()