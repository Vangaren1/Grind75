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
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max( self.maxDepth(root.left), self.maxDepth(root.right))
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            leftIsBalanced = self.isBalanced(root.left)
            rightIsBalanced = self.isBalanced(root.right)
            difference = abs( self.maxDepth(root.left) - self.maxDepth(root.right))
            return difference <= 1 and leftIsBalanced and rightIsBalanced
            
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    s = Solution()
    
    allPass = True
    errorMsg = "Value not correct"
    
    root = [3,9,20,15,7]
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result1 = s.isBalanced(root)
    
    try:
        assert result1 == True, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    
    
    result1 = s.isBalanced(root)
    
    try:
        assert result1 == False, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    


    if allPass:    
        print("Passes all test cases")
    