from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self, root):
        if root is None:
            return 0
        return max( 1 + self.depth(root.left), 1 + self.depth(root.right) )
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        rightDepth = self.depth(root.right)
        leftDepth = self.depth(root.left)
        return abs(rightDepth - leftDepth) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)
        

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()

print(sol.isBalanced(root))


root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.left.right = TreeNode(4)
root.left.left.left = TreeNode(4)

print(sol.isBalanced(root))