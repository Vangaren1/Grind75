from typing import List, Optional

"""
Below is the leetcode solution

"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}
        
        def dfs(node: Node):
            if node in hashMap:
                return hashMap.get(node)
            newNode = Node(val = node.val)
            hashMap[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
            return newNode
        
        dfs(node)
        
        return hashMap.get(node)
            
            
            
        
        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    first = Node(val=1)
    second = Node(val=2)
    third = Node(val=3)
    fourth = Node(val=4)
    
    first.neighbors = [second, fourth]
    second.neighbors = [first, third]
    third.neighbors = [second, fourth]
    fourth.neighbors = [first, third]
    
    result1 = sol.cloneGraph(first)
    
    try:
        assert result1 == 5, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    