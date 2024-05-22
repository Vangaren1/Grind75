from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def fullAdder(a, b, c):
            first = a == '1'
            second = b == '1'
            carry = c == '1'
            ab = ( first ^ second)
            bitOut = ab ^ carry
            carryOut = ( first and second ) or ( carry and ab )
            return (bitOut, carryOut)
        carryIn = '0'
        output = ''
        while a and b:
            first = a[-1]
            a = a[:-1]
            second = b[-1]
            b = b[:-1]
            outBit, carryOut = fullAdder(first, second, carryIn)
            outBit = '1' if outBit else '0'
            carryIn = '1' if carryOut else '0'
            output += outBit 
        
        leftover = a if len(a) > 0 else b
        if len(leftover) > 0:
            leftover = self.addBinary(leftover, carryIn)
            leftover = leftover[::-1]
        else: 
            leftover = '1' if carryIn == '1' else ''

        output += leftover

        return output[::-1]
    

"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    a = "11"
    b = "1"
    expected = '100'


    result1 = sol.addBinary('10','1000010')
    
    try:
        assert result1 == '110', errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    