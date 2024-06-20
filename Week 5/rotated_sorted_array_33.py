from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        
        start = 0
        end = length
        while start < end:
            # calculate middle
            mid = (start + end) // 2
            
            # see if middle point is target:
            if nums[mid] == target:
                return mid
            
            # see if left is sorted 
            if nums[start] < nums[mid]:
                # if it is sorted, see if target is inside
                if nums[start] <= target <= nums[mid]:
                    # if it is in the range, search only in the left half
                    end = mid
                else:
                    # otherwise, check the right unsorted half
                    start = mid
            else:
                # if left is unsorted, then right is
                # check if target is in right 
                if nums[mid] <= target <= nums[end - 1]:
                    # if it is, set the next loop to search right half
                    start = mid
                else:
                    # if it isn't, then it's in the left
                    end = mid
        
        # if the loop breaks, that means start >= end, and the target wasn't found
        return -1
                
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    nums = [1]
    target = 0
    expected = -1
    result = sol.search(nums, target)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    