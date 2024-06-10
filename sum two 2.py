from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int, skip, start) -> List[int]:
        index = start
        end = len(numbers) - 1
        seen = set()
        retList = []
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
            if s == target:
                tmp = (index + 1, end + 1)
                if tmp not in seen:
                    retList.append([tmp1, tmp2])
                index += 1
            elif s < target:
                index += 1
            else:
                end -= 1
        return retList
                


"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    numbers = [2,2,7,11,15]
    target = 9
    output = [1,2]

    result1 = sol.twoSum(numbers, target, 1, 0)
    
    try:
        assert result1 == output, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    