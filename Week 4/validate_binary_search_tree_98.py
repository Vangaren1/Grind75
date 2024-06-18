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
                if len(order) > 1 and order[-2] >= order[-1]:
                    raise Exception(False)
                traverse(root.right)
            return True
        try:
            check = traverse(root)
        except:
            return False
        return check

        

        
    
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
    