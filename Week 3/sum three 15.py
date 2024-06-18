from typing import List, Optional

def threeSumOld(self, nums: List[int]) -> List[List[int]]:
    length = len(nums)
    sortedCopy = [ (nums[i], i) for i in range(length)]
    sortedCopy.sort(key=lambda x: x[0])
    # print([ s[0] for s in sortedCopy])
    index = 0
    retList = []
    seen = set()
    while index < (length - 2):
        first = sortedCopy[index]
        secondIndex = index + 1
        thirdIndex = length - 1
        while secondIndex < thirdIndex:
            if index > (length -2):
                break
            tmp1 = sortedCopy[secondIndex]
            tmp2 = sortedCopy[thirdIndex]
            sum = -1 * (tmp1[0] + tmp2[0])
            pairing = (first, tmp1, tmp2)
            if sum == first[0] and pairing not in seen:
                seen.add(pairing)
                retList.append( [ first, tmp1, tmp2] )
                index += 1
            elif sum < first[0]:
                secondIndex += 1
            elif sum > first[0]:
                thirdIndex -= 1 
            
        index += 1
    return retList

"""
Below is the leetcode solution

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        retVal = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp = a + nums[j] + nums[k]
                if tmp > 0:
                    k -= 1 
                elif tmp < 0:
                    j += 1
                else:
                    retVal.append([a, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return retVal
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    nums = [-1,0,1,2,-1,-4]
    Output = [[-1,-1,2],[-1,0,1]]

    result = sol.threeSum(nums)
    
    try:
        assert result == 5, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    