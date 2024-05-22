from typing import List

"""
Below is the leetcode solution

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        for i in range(0, length):
            for j in range( i , length ):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
                
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    errorMsg = "Value not correct"
    
    result1 = s.twoSum([2,7,11,15], 9)
    assert result1 == [0,1] , errorMsg
    
    result2 = s.twoSum([2,5,5,11], 10)
    assert result2 == [1,2] , errorMsg
    
    result3 = s.twoSum([3,2,4], 6)
    assert result3 == [1,2] , errorMsg
    
    print("Passes all test cases")
    