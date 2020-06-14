class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        
        
    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        res = self.stack1.pop()
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return res

    
    def peek(self):
        """
        Get the front element.
        """
        n = len(self.stack1) - 1
        for i in range(n):
            self.stack2.append(self.stack1.pop())
        res = self.stack1[0]
        for i in range(n):
            self.stack1.append(self.stack2.pop())
        return res

    
    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()