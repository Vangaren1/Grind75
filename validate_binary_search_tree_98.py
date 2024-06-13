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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        def traverse(root):
            if root:
                traverse(root.left)
                order.append(root.val)
                traverse(root.right)
        traverse(root)
        if len(order) <= 1:
            return True
        for index in range(1, len(order)):
            if order[index - 1] >= order[index]:
                return False
        return True
        

        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    
    result1 = sol.isValidBST(root)

    try:
        assert result1 == True, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    