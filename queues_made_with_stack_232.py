from typing import List, Optional

"""
Below is the leetcode solution

"""
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, y):
        self.stack.insert(0, y)
    def pop(self):
        return self.stack.pop(0)
    def peek(self):
        return self.stack[0]
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size() == 0

class MyQueue:
    class Stack:
        def __init__(self):
            self.stack = []
        def push(self, y):
            self.stack.insert(0, y)
        def pop(self):
            return self.stack.pop(0)
        def peek(self):
            return self.stack[0]
        def size(self):
            return len(self.stack)
        def isEmpty(self):
            return self.size() == 0
    def __init__(self):
        self.queue = Stack()
        
    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        tmp = Stack()
        while not self.empty():
            tmp.push( self.queue.pop() )
        returnVal = tmp.pop()
        while not tmp.isEmpty():
            self.queue.push( tmp.pop() )
        return returnVal
        
    def peek(self) -> int:
        tmp = Stack()
        while not self.empty():
            tmp.push( self.queue.pop() )
        returnVal = tmp.peek()
        while not tmp.isEmpty():
            self.queue.push( tmp.pop() )
        return returnVal

    def empty(self) -> bool:
        return self.queue.isEmpty()
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = MyQueue()
    
    allPass = True
    errorMsg = "Value not correct"
    
    # ["MyQueue","push","push","peek","pop","empty"]
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
    
    
    # result1 = sol
    
    # try:
    #     assert result1 == 5, errorMsg.format(result1)
    # except Exception as e: 
    #     allPass = False
    #     print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    