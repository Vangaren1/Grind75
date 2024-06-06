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
    sums = {}
    def twoSum(self, numbers: List[int], target: int, skip, start) -> List[int]:
        index = start
        end = len(numbers) - 1
        seen = set()
        retList = []
        if target in self.sums:
            return self.sums[target]
        while index < end:
            if index == skip:
                index += 1
                continue
            if end == skip:
                end -= 1
                continue            
            tmp1 = numbers[index]
            tmp2 = numbers[end]
            s = tmp1 + tmp2 
            self.sums[ s ] = (index, end)
            if s == target:
                tmp = (index, end)
                if tmp not in seen:
                    retList.append(tmp)
                index += 1
            elif s < target:
                index += 1
            else:
                end -= 1
        return retList
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedList = nums.copy()
        sortedList.sort()
        seen = set()
        for index in range(len(nums)):
            target = sortedList[index] * -1
            pairs = self.twoSum(sortedList, target, index, index)
            if len(pairs) > 0:
                p = [ (sortedList[index], sortedList[pair[0]], sortedList[pair[1]]) for pair in pairs ]
                for n in p:
                    seen.add(n)
        return [ [s[0], s[1], s[2]] for s in seen]
    
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
    