from typing import List, Optional

"""
Below is the leetcode solution

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        last = None
        count = 0
        def traverse(node: Optional[TreeNode]):
            nonlocal last, count
            if node:
                traverse(node.left)
                last = node.val
                count += 1
                if count == k:
                    raise Exception()
                traverse(node.right)
        try:
            traverse(root)
        except:
            return last

"""
Tree Node generator
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    null = None
    root = [5,3,6,2,4,None,None,1]
    root = deserialize(root)
    k = 3

    expected = 3
    result = sol.kthSmallest(root, k)

    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    