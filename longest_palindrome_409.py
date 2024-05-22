from typing import List, Optional
from collections import defaultdict


"""
Below is the leetcode solution

"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        def isEven(n):
            return n%2 == 0
        def maxUsable(m):
            if isEven(m):
                return m
            else:
                return m-1
        sDict = defaultdict(int)
        for char in s:
            sDict[char] += 1
        sum = 0
        hasOdd = False
        for v in sDict.values():
            if not isEven(v):
                hasOdd = True
            sum += maxUsable(v)
        if hasOdd:
            sum += 1
        return sum
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    input = ["abccccdd", "a" ]
    expected = [7, 1]
    
    try:
        for i in range(len(input)):    
            result1 = sol.longestPalindrome(input[i])
            assert result1 == expected[i], errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    