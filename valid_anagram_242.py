from typing import List
from collections import defaultdict

"""
Below is the leetcode solution

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        
        for char in s: 
            sDict[char] += 1
        for char in t: 
            tDict[char] += 1
        
        return sDict == tDict
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct.  Value: {}"
    
    s = "anagram" 
    t = "nagaram"
    
    result1 = sol.isAnagram(s,t)

    try:
        assert result1 == True, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    