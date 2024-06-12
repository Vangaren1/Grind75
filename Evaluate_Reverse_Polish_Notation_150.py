from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        func = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: y - x,
            "*": lambda x,y: x * y,
            "/": lambda x,y: int(y / x)
        }
        while len(tokens) > 0:
            tmp = tokens.pop(0)
            if tmp not in "+-*/":
                stack.insert(0,int(tmp))
            else:
                a = stack.pop(0)
                b = stack.pop(0)
                result = func[tmp](a,b)
                stack.insert(0,result)
        return stack[0]

"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    expected = 22

    result1 = sol.evalRPN(tokens)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    