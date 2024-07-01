from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        tmp = ""
        result = 0
        isNegative = False
        ptr = 0
        s = s.strip()
        if ptr == len(s):
            return 0
        if s[ptr] in ('-', '+'):
            isNegative = s[ptr] == '-'
            s = s[1:]
        if ptr == len(s):
            return 0
        while s[ptr].isdigit():
            tmp += s[ptr]
            ptr += 1
            if ptr == len(s):
                break
        tmp = tmp[::-1]
        for index, char in enumerate(tmp):
            result += 10**index * (ord(char) - ord('0'))
        if isNegative:
            result *= -1
        if result < -2147483648:
            return -2147483648
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
            


        
        
        
        
        pass 
    




"""
Tree Node generator
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

null = None

def deserialize(treeList):
    if len(treeList) == 0:
        return None
    nodes = [ TreeNode(val) if val is not None else None for val in treeList ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

"""
Testing Below this

"""
    




if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    num = " -"

    expected = 0
    result = sol.myAtoi(num)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    