from typing import List, Optional
from collections import defaultdict

"""
Below is the leetcode solution

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        highestNum = -1
        highestCount = 0
        length = len(nums)
        for i in range(length):
            count[nums[i]] += 1
            if count[nums[i]] > highestCount:
                highestCount = count[nums[i]]
                highestNum = nums[i]
        return highestNum


"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    nums = [3,3,4]
    expected = 3

    result1 = sol.majorityElement(nums)
    


    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    