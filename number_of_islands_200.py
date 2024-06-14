from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        mLen = len(grid)
        nLen = len(grid[0])
        count = 0
        def bfs(pos):
            queue = [pos]
            fourWays = [(1,0),(-1,0),(0,1),(0,-1)]
            while len(queue)>0:
                y,x = queue.pop(0)
                seen.add((y,x))
                for dir in fourWays:
                    tmp = (y+dir[0], x+dir[1])
                    newX, newY = tmp
                    if 0 <= newX < nLen and 0 <= newY < mLen:
                        if tmp not in seen and grid[newY][newX] == "1" and tmp not in queue:
                            queue.append(tmp)
        for i in range(mLen):
            for j in range(nLen):
                if grid[i][j] == "1" and (j,i) not in seen:
                    count += 1
                    bfs((j,i))
        return count
                        
                    
                
        pass 
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ]
    
    result1 = sol.numIslands(grid)
    expected = 3
    
    try:
        assert result1 == expected, errorMsg.format(result1)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    