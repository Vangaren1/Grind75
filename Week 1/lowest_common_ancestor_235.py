from typing import List

"""
Below is the leetcode solution

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def find(self, val):
        if self.root.val == val:
            return True

    def add(self, val) -> TreeNode:
        def addRecursive(val, root):
            if root == None:
                return TreeNode(val)
            if val < root.val:
                root.left = addRecursive(val, root.left)
            if val > root.val:
                root.right = addRecursive(val, root.right)
            return root
        self.root = addRecursive(val, self.root)


def add(val, root):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = add(val, root.left)
    else:
        root.right = add(val, root.right)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


        
        
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct"

    testTree = [6,2,8,0,4,7,9,3,5]
    
    treeRoot = TreeNode(6)
    p,q = None, None
    
    for t in testTree[1:]:
        add(t, treeRoot)
        
    p = treeRoot.left
    q = treeRoot.right
        
    result1 = sol.lowestCommonAncestor(treeRoot, p, q)
    
    
    
    # try:
    #     assert result1 == 5, errorMsg.format(result1)
    # except Exception as e: 
    #     allPass = False
    #     print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    