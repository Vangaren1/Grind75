from typing import List, Optional

"""
Below is the leetcode solution

"""
class MinStack: 

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.isEmpty():
            newMin = self.getMin() 
            newMin = val if val < newMin else newMin
        else:
            newMin = val
        self.stack.insert(0,(val,newMin))

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0


"""
Testing Below this

"""
    
if __name__ == "__main__":
        
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
    # [null,null,null,null,-3,null,0,-2]
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())



    
    if allPass:    
        print("Passes all test cases")
    