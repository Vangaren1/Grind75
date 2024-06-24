from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlaps(first, second):
            if first is None or second is None:
                return False
            if second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]:
                return True
            if first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
                return True
            return False
        intervals.sort(key=lambda x: x[0])
        ptr = 0
        # ptr points to the currently examined interval
        # because the length of intervals may change 
        while ptr < len(intervals):
            curr = intervals[ptr]
            # check the next interval, see if it overlaps
            nextInt, prev = None, None
            if ptr != len(intervals) -1:
                nextInt = intervals[ptr+1]
            if ptr > 0:
                prev = intervals[ptr - 1]
            if overlaps(curr, nextInt):
                tmp = [min(curr[0], nextInt[0]), max(curr[1], nextInt[1])]
                intervals.pop(ptr)
                intervals[ptr] = tmp
            elif ptr > 0 and overlaps(curr, prev):
                tmp = [min(curr[0], prev[0]), max(curr[1], prev[1])]
                intervals.pop(ptr)
                ptr -= 1
                intervals[ptr] = tmp
            else:
                ptr += 1
        return intervals

        pass 
    




"""
Tree Node generator
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

null = None

def deserialize(treeList):
    if len(treeList) == 0:
        return None
    nodes = [ TreeNode(val) if val is not None else None for val in treeList ]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

"""
Testing Below this

"""
    




if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]

    expected = [[1,6],[8,10],[15,18]]
    result = sol.merge(intervals)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    