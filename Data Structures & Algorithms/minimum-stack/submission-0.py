class MinStack:

    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val,0])
        else:
            prev = self.stack[-1]
            curMinIndx  = prev[1]
            if val < self.stack[curMinIndx][0]:
                self.stack.append([val,len(self.stack)])
            else:
                self.stack.append([val,curMinIndx])

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        curr = self.stack[-1]
        minIndx = curr[1]
        return self.stack[minIndx][0] 
