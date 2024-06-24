from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        seen = set()
        if len(nums) == 1:
            return [nums]
        def recursive(remaining):
            if remaining == []:
                return 
            if len(remaining) == 1:
                return remaining
            tmp = []
            for i in range(len(remaining)):
                val = remaining[i]
                rem = recursive(remaining[:i] + remaining[i+1:])
                for r in rem:
                    r = [r] if type(r) != list else r
                    r = [val] + r
                    tmp.append(r)
            return tmp
        return recursive(nums)




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

    nums = [1]
    expected = 5
    result = sol.permute(nums)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    