from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    maxMinutes = 0
    goodOranges = 0
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        lenX = len(grid)
        lenY = len(grid[0])
        seen = set()
        self.maxMinutes = 0
        def bfs(pos):
            minutes = 0
            queue = [(pos[0],pos[1],minutes)]
            while len(queue) > 0:
                tmp = queue.pop(0)
                x,y, minutes = tmp
                self.maxMinutes = max(self.maxMinutes, minutes)
                if grid[x][y] == "@":
                    seen.add((x,y))
                    for dir in directions:
                        adjx, adjy = x + dir[0], y + dir[1]
                        if 0 <= adjx < lenX and 0 <= adjy < lenY and (adjx, adjy) not in seen:
                            if grid[adjx][adjy] >= 1:
                                grid[adjx][adjy] = min(minutes , grid[adjx][adjy])
                                self.goodOranges -= 1
                                queue.append((adjx, adjy, minutes+1))
        for i in range(lenX):
            for j in range(lenY):
                if grid[i][j] == 2:
                    grid[i][j] = '@'
                if grid[i][j]==1:
                    self.goodOranges += 1
        for i in range(lenX):
            for j in range(lenY):
                bfs((i,j))
        return self.maxMinutes if self.goodOranges == 0 else -1
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"

    grid = [[2,1,1],
            [1,1,0],
            [0,1,2]]

    

    expected = 4
    result = sol.orangesRotting(grid)
    
    if result is not None:
        for r in result:
            print(r)

    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    