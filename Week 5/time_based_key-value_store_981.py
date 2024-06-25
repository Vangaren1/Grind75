from typing import List, Optional

"""
Below is the leetcode solution

"""

class TimeMap:

    def __init__(self):
        self.baseDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.baseDict:
            self.baseDict[key].append((value, timestamp))
        else:
            self.baseDict[key] = [("",0), (value, timestamp)]
             

    def get(self, key: str, timestamp: int) -> str:
        baseArray = self.baseDict.get(key)
        if baseArray:
            ptr = -1
            last = baseArray[ptr]
            while (last[1] > timestamp):
                last = baseArray[ptr]
                ptr -=1
            return last[0]
        return ""
        



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
    
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    cmds = ["TimeMap", "set", "get", "get", "set", "get", "get"]
    actions = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    tm = TimeMap()
    print(tm.set("foo", "bar", 1))
    print(tm.set("foo", "none", 5))
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))
    print(tm.get("foo", 6))
    

    output = [null, null, "bar", "bar", null, "bar2", "bar2"]

    expected = 5

    

    if allPass:    
        print("Passes all test cases")
    