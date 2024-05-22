from typing import List

"""
Below is the leetcode solution

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [ c.lower() for c in s if c.isalnum() ]
        left,right=0,len(chars)-1
        while left<right:
            if chars[left] != chars[right]:
                return False
            left += 1 
            right -= 1        
        return True

        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    allPass = True
    errorMsg = "Value not correct"
    
    test1 = "A man, a plan, a canal: Panama"
    result1 = s.isPalindrome(test1)
    
    try:
        assert result1 == True, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))
    
    test2 = "race a car"
    result2 = s.isPalindrome(test2)
    
    try:
        assert result2 == False, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("second test failed: {}".format(e))
    
    if allPass:
        print("Passes all test cases")
    