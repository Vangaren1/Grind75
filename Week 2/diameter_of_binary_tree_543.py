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
    maximum = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # if the root is None, then it's a empty branch
            if root is None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.maximum = max(self.maximum, left + right + 2)
            return 1 + max( left, right )
        self.maximum = 0
        dfs(root)
        return self.maximum
    
            
        


    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    result1 = sol
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result1 = sol.diameterOfBinaryTree(root)
    expected = 3

    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    root = TreeNode(1)
    root.left = TreeNode(2)
    expected = 1
    
    result1 = sol.diameterOfBinaryTree(None)
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))
    if allPass:    
        print("Passes all test cases")
    