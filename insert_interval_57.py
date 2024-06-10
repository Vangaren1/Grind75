from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0] = min( newInterval[0], intervals[i][0])
                newInterval[1] = max( newInterval[1], intervals[i][1])
        res.append(newInterval)
        return res

        
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    interval = [[1,3],[6,9]]
    newInterval = [2,5]
    Output= [[1,5],[6,9]]
    
    result1 = sol.insert(interval, newInterval)
    
    try:
        assert result1 == Output, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))
        
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    output = [[1,2],[3,10],[12,16]]
    
    result = sol.insert(intervals, newInterval)

    print(result)
    
    if allPass:    
        print("Passes all test cases")
    