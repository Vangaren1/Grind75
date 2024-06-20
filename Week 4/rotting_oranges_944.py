from typing import List, Optional

"""
Below is the leetcode solution

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(pos):
            def isValid(pos):
                return 0 <= pos[0] < lenM and 0 <= pos[1] < lenN and pos not in seen
            seen = set()
            queue = [(pos[0],pos[1], 0)]
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                tmp = queue.pop(0)
                x,y,minute = tmp
                seen.add((x,y))
                
                for dir in directions:
                    adjx = x + dir[0]
                    adjy = y + dir[1]
                    
                    if isValid((adjx, adjy)) and grid[adjx][adjy] != 0:
                        if grid[adjx][adjy] == '@':
                            continue
                        newVal = min(grid[adjx][adjy], minute + 1)
                        grid[adjx][adjy] = newVal
                        queue.append( (adjx, adjy, minute + 1 ) )
        
        lenM = len(grid)
        lenN = len(grid[0])
        
        startingOrange = []
        # set 2's to "@" and all 1's to float(inf)
        for i in range(lenM):
            for j in range(lenN):
                if grid[i][j] == 2:
                    grid[i][j] = '@'
                    startingOrange.append((i,j))
                elif grid[i][j] == 1:
                    grid[i][j] = float('inf')
             
        #preform BFS starting from each rotten orange
        for starting in startingOrange:
            bfs(starting)
            
        # find highest num in the grid and if any oranged remain
        highest = 0
        for i in range(lenM):
            for j in range(lenN):
                tmp = grid[i][j]
                if tmp == float('inf'):
                    return -1
                elif tmp == '@':
                    grid[i][j] = 0
                highest = max(highest, grid[i][j])
        return highest
    
    
"""
Testing Below this

"""
    
if __name__ == "__main__":
    sol = Solution()
    
    allPass = True
    errorMsg = "Value not correct, Value: {}"
    
    grid = [[0,2]]
    expected = 4
    result = sol.orangesRotting(grid)
    
    try:
        assert result == expected, errorMsg.format(result)
    except Exception as e: 
        allPass = False
        print("first test failed: {}".format(e))

    if allPass:    
        print("Passes all test cases")
    