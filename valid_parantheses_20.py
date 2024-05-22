from typing import List

"""
Below is the leetcode solution

"""
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        left  = {'(':0, '[':1, '{':2}
        right = {')':0, ']':1, '}':2}
        
        match = {'(':')', '[':']', '{':'}'}
        
        for char in s:
            if char in left:
                stack.append(char)
            if char in right:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if char != match[tmp]:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True
        
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    errorMsg = "Value not correct, value given: {}"
    
    # result1 = s.twoSum([2,7,11,15], 9)
    # assert result1 == [0,1] , errorMsg
    
    result1 = s.isValid("()") 
    assert result1 == True, errorMsg.format(result1)
    
    result2 = s.isValid("()[]{}") 
    assert result2 == True, errorMsg.format(result2)
    
    result3 = s.isValid("(]") 
    assert result3 == False, errorMsg.format(result3)

    print("Passes all test cases")
    