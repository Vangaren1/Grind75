from typing import List, Optional
import math

"""
Below is the leetcode solution

"""

class Solution:
    class minQ:
        def __init__(self) -> None:
            self.q = []
        def insert(self, val):
            if len(self.q) == 0:
                self.q.append(val)
                return
            first = self.q[0][0]
            last = self.q[-1][0] 
            if last < val[0]:
                self.q.append(val)
            elif val[0] <= first:
                self.q.insert(0, val)
            else:
                i = 0
                while True:
                    if self.q[i] < val[0] <= self.q[i+1]:
                        self.q.insert(i+1, val)
                        break
                    i += 1
        def pop(self):
            return self.q.pop(0)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(pos):
            x, y = pos
            dist = math.sqrt( x**2 + y**2 )
            return dist
        minQueue = self.minQ()
        
        for p in points:
            dist = distance(p)
            minQueue.insert((dist, p))
            
        
        retList = []
        for i in range(k):
            val = minQueue.pop()
            retList.append(val[1])
        
        return retList
        
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    points = [[0,1],[1,0]]
    k = 2
       
    output = [[3,3],[-2,4]]
    
    result1 = sol.kClosest(points, k)
    
    
    
    try:
        assert result1 == output, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    