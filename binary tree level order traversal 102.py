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
    queue = []
    def traverse(self, root, level):
        if root is not None:
            self.queue.append((root.val, level))
            self.traverse(root.left, 1 + level)
            self.traverse(root.right, 1 + level)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0)
        retList = []
        index = 0
        while len(self.queue) > 0:
            val, level = self.queue.pop(0)
            if level + 1 <= len(retList):
                retList[level].append(val)
            else:
                retList.append([val])
                index += 1

            
        return retList
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    expected = [[3],[9,20],[15,7]]

    result1 = sol.levelOrder(root)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    