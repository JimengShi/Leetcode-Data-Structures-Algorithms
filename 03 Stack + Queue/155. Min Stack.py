# Approach 1: Stack of Value/ Minimum Pairs
class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:        
        # If the stack is empty, then the min value must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
          
    def pop(self) -> None:
        if not self.stack:
            return None
        self.stack.pop()        

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]
    
# Time: O(1) for all operations
# Space: O(N) for a stack with length of N
    
    
# Approach 2: Two Stacks    
class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, x):
        self.items.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        if not self.items:
            return None
        item = self.items.pop()
        if item == self.min[-1]:
            self.min.pop() 
        return item 
    
    def top(self):
        if not self.items:
            return None
        return self.items[-1]

    def getMin(self):
        if not self.min: 
            return None
        return self.min[-1]
    
# Time: O(1) for all operations
# Space: O(N) for a stack with length of N