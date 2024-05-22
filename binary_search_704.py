from typing import List

"""
Below is the leetcode solution

"""
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        mid = end // 2
        while nums[mid] != target:
            if target < nums[start]:
                return -1
            if target > nums[end]:
                return -1
            if nums[mid] < target:
                start = mid +1
            else:
                end = mid - 1
            mid = (end + start+1) // 2
        return mid
        
            
                
                 
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, value:{}"
    
    nums = [2,5]
    target = 5
    result1 = sol.search(nums, target)
    
    try:
        assert result1 == 1, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    nums = [-1,0,3,5,9,12]
    target = 14
    result1 = sol.search(nums, target)

    try:
        assert result1 == -1, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    nums = [-1,0,3,5,9,12]
    target = 2
    result1 = sol.search(nums, target)

    try:
        assert result1 == -1, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    nums = [-1,0,5]
    target = -1
    result1 = sol.search(nums, target)

    try:
        assert result1 == 0, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    