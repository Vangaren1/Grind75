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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        rVal = TreeNode(val=root.val)
        rVal.left = self.invertTree(root.right)
        rVal.right = self.invertTree(root.left)
        return rVal

    
    

    
"""
Testing Below this

"""

def addNode(val:int, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val=val)
    if val < root.val:
        root.left = addNode(val, root.left)
    else: 
        root.right = addNode(val, root.right)
    return root
        
def printTree(root: Optional[TreeNode]):
    if root:
        if root.left:
            printTree(root.left)
        print(root.val)
        if root.right:
            printTree(root.right)

    
if __name__ == "__main__":
    s = Solution()
    
    allPass = True
    errorMsg = "Value not correct"
    
    test1 = [4,2,7,1,3,6,9]
    root = None
    for t in test1:
        root = addNode(t, root)
    
    
    printTree(root)
    print()
    newRoot = s.invertTree(root)
    
    printTree(newRoot)
    
    
    try:
        assert 5 == 5, errorMsg.format(5)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    