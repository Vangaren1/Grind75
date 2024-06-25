from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # determine if node a is a child of or is node b
        if root in (None, p, q):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left 
        return root
    




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

    root = [3,5,1,6,2,0,8,null,null,7,4]
    root = deserialize(root)

    p = root
    q = root.left.right.right
    expected = root.left.right
    result = sol.lowestCommonAncestor(root, p, q)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    