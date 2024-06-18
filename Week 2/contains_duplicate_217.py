from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    result1 = sol

    nums = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
    expected = [True, False, True]
    
    for i in range(len(nums)):
        result1 = sol.containsDuplicate(nums[i]) 
        try:
            assert result1 == expected[i], errorMsg.format(result1)
        except Exception as e: 
            allPass = False
            print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    