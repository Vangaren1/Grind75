from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [ 1 for _ in nums ]
        suffix = [ 1 for _ in nums ]
        length = len(nums)

        for index in range(1, length):
            prefix[index] = prefix[index - 1] * nums[index - 1]
        for index in range(length - 2, -1, -1):
            suffix[index] = suffix[index + 1] * nums[index + 1]
        
        answer = [ prefix[index] * suffix[index] for index in range(length)]
        return answer




    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    nums = [-1,1,0,-3,3]
    expected = [0,0,9,0,0]
    
    result1 = sol.productExceptSelf(nums)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    nums = [-1,1,0,-3,3]
    Output = [0,0,9,0,0]
 

    if allPass:    
        print("Passes all test cases")
    