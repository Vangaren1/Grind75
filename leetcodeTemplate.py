from typing import List, Optional

"""
Below is the leetcode solution

"""
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct"
    
    result1 = sol
    
    try:
        assert result1 == 5, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    